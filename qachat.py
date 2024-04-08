import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  

# setting up api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# initialize model and chat history
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# function to load gemini pro and chat 
def chat_with_gemini(question):
    response = chat.send_message(question)
    return response.text

# creating chat history in streamlit session
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# setting streamlit UI
st.title("Chat with Gemini-pro")
input_text = st.text_input("Say something")
submit_button = st.button("Submit")
show_history_button = st.button("Show History")

if submit_button and input_text:
    response = chat_with_gemini(input_text)
    st.write("You:", input_text)
    st.write("Gemini-pro:", response)
    st.session_state.chat_history.append(("You", input_text))
    st.session_state.chat_history.append(("Gemini-pro", response))

# Show chat history if requested
if show_history_button:
    st.subheader("Chat History")
    for user, message in st.session_state.chat_history:
        st.write(f"{user}: {message}")
