import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer
@st.cache_resource
def load_model():
    model_name = "microsoft/DialoGPT-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("Offline AI Chatbot")

# Display chat history
for message in st.session_state.chat_history:
    if message['role'] == 'user':
        st.write(f"**You:** {message['text']}")
    else:
        st.write(f"**Bot:** {message['text']}")

# User input
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({'role': 'user', 'text': user_input})

        # Encode the conversation history
        chat_history_ids = None
        for message in st.session_state.chat_history:
            if message['role'] == 'user':
                new_user_input_ids = tokenizer.encode(message['text'] + tokenizer.eos_token, return_tensors='pt')
                if chat_history_ids is not None:
                    chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
                else:
                    chat_history_ids = new_user_input_ids
            else:
                bot_input_ids = tokenizer.encode(message['text'] + tokenizer.eos_token, return_tensors='pt')
                if chat_history_ids is not None:
                    chat_history_ids = torch.cat([chat_history_ids, bot_input_ids], dim=-1)
                else:
                    chat_history_ids = bot_input_ids

        # Generate response
        with torch.no_grad():
            response_ids = model.generate(chat_history_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # Decode the response
        response = tokenizer.decode(response_ids[:, chat_history_ids.shape[-1]:][0], skip_special_tokens=True)

        # Add bot response to history
        st.session_state.chat_history.append({'role': 'bot', 'text': response})

        # Clear input
        st.experimental_rerun()
