import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Check for API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Google API key not found. Please set it in your .env file.")
    st.stop()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",
    layout="centered",
)

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)

# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Input field for user's message
user_prompt = st.text_input("Ask Gemini-Pro...")

if user_prompt:
    # Display user's message
    st.write(f"You asked: {user_prompt}")

    try:
        # Send user's message to Gemini-Pro and get the response
        model = gen_ai.GenerativeModel('gemini-pro')
        response = model.send_message(user_prompt)

        # Display Gemini-Pro's response
        st.write(f"Response: {response.text}")
        
    except Exception as e:
        st.error(f"An error occurred while communicating with the API: {str(e)}")
