# Offline AI Chatbot
**Read License First**
 
This is a simple offline AI chatbot built using Streamlit and Hugging Face Transformers. It uses the Microsoft DialoGPT-small model for conversational AI, running entirely offline after the initial model download.

## Features

- Conversational AI using DialoGPT-small
- Web-based interface with Streamlit
- Runs offline after setup
- Maintains chat history during the session

## Setup Instructions

1. **Clone or download the project files.**

2. **Set up a virtual environment (recommended):**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
   Note: The first run will download the AI model, which may take some time and requires internet access.

4. **Run the chatbot:**
   ```
   streamlit run app.py
   ```

5. **Access the chatbot:**
   Open your web browser and go to the URL provided by Streamlit (usually http://localhost:8501).

## Usage

- Type your message in the input box and click "Send".
- The chatbot will respond based on the conversation history.
- The chat history is maintained for the current session.

## Requirements

- Python 3.7+
- Internet access for initial model download (subsequent runs are offline)

## Notes

- The model is small for faster loading and lower resource usage, but responses may be less sophisticated.
- For better performance, consider using a more powerful model if your hardware allows.
