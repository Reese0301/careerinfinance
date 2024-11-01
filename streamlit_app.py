import streamlit as st
import requests

# Show title and description.
st.title("💬 Career Advisor in Finance")
st.write(
    "This chatbot answers Finance recruiting questions."
    "To use this app, enter your query in the chat below."
)

# Set your Flowise API URL
API_URL = "https://flowise-9kx9.onrender.com/api/v1/prediction/cef2a608-65a9-4813-a3a7-171a153c40b3"

# Function to send queries to the API
def query(payload):
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("text")
    else:
        return f"Error: {response.status_code}"

# Initialize the session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input field for user to enter a message
if prompt := st.chat_input("Ask your question here..."):

    # Store and display the user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the query to your custom API
    response_content = query({"question": prompt})
    
    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(response_content)
    st.session_state.messages.append({"role": "assistant", "content": response_content})

