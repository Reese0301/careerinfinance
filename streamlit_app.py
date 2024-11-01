import streamlit as st
import requests

# Show title and description.
st.title("💬 Career Advisor in Finance")
st.markdown(
    """
    - This AI Agent answers questions regarding Finance and Investment Banking Recruiting.
    - Talk with the AI by entering your query in the chatbox below.
    - To provide accurate and high-performance answers, this AI Agent was built using a multiple-agent framework.
    - Processing time can be slower than ChatGPT, please wait patiently while the AI is running.
    """
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
    # Add a default welcome message from the assistant
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Hello! I'm here to assist you with any finance and investment banking recruiting questions you may have. How can I help you today?"
    })

# Display existing chat messages with profile pictures
for message in st.session_state.messages:
    if message["role"] == "user":
        # Use a GitHub placeholder image for the user
        with st.chat_message("user", avatar="https://github.com/Reese0301/GIS-AI-Agent/blob/main/FoxUser.png?raw=true"):
            st.markdown(message["content"])
    else:
        # Use a different GitHub placeholder for the assistant
        with st.chat_message("assistant", avatar="https://github.com/Reese0301/GIS-AI-Agent/blob/main/4322991.png?raw=true"):
            st.markdown(message["content"])

# Chat input field for user to enter a message
if prompt := st.chat_input("Ask your question here..."):

    # Store and display the user's message with the user avatar
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="https://github.com/Reese0301/GIS-AI-Agent/blob/main/FoxUser.png?raw=true"):
        st.markdown(prompt)

    # Send the query to your custom API
    response_content = query({"question": prompt})

    # Display the assistant's response with the assistant avatar
    with st.chat_message("assistant", avatar="https://github.com/Reese0301/GIS-AI-Agent/blob/main/4322991.png?raw=true"):
        st.markdown(response_content)
    st.session_state.messages.append({"role": "assistant", "content": response_content})
