import streamlit as st
import google.generativeai as genai

st.title('Welcome to my chat ')



genai.configure(api_key="AIzaSyCZ7RjMK3mg5HqV6LiGl60KBykOH-a1cCs")

text = st.text_input("Enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("GO"):
    response = chat.send_message(text)
    st.write(response.text)

