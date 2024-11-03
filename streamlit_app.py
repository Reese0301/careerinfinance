import streamlit as st
import requests
import random
import time  # Import the time module for tracking response time

# Set your Flowise API URL
API_URL = st.secrets["API_URL"]

# List of randomized "thinking" messages
thinking_messages = [
    "Alex is Crunching the numbers…",
    "Running a DCF… please hold for a valuation.",
    "Checking with the M&A team… Alex will be right back.",
    "Consulting the deal book…",
    "Reviewing the pitch deck… insights coming soon.",
    "Adjusting the financial model…",
    "Running a few more Monte Carlo simulations… hang tight!",
    "Preparing a high-stakes IPO answer… patience pays dividends.",
    "Just a moment… Alex is cutting through red tape.",
    "The market's in flux… recalibrating!"
]

# Function to send queries to the API
def query(payload):
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("text")
    else:
        return f"Error: {response.status_code}"

# Main content: Chat interface
st.title("💬 Alex, Career Advisor in Finance")
st.markdown(
    """
    - Alex is an AI Agent that answers your questions regarding Finance and Investment Banking Recruiting.
    - To provide accurate and high-performance answers, Alex was built using a multiple-agent framework. 
    - 🧠 This enables him to deliver valuable insights with sharper reasoning than ChatGPT.
    - 🚥 Processing time can be slower than ChatGPT, please wait patiently while the AI is running.
    - Talk with him by entering your question in the chatbox below.
    """
)

# Initialize the session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add a default welcome message from the assistant
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Hello! I'm here to assist you with any finance recruiting questions you may have. How can I help you today?"
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

    # Display a random "Alex is thinking..." message
    thinking_message = random.choice(thinking_messages)
    thinking_placeholder = st.empty()
    thinking_placeholder.markdown(f"💭 **{thinking_message}**")

    # Start the timer
    start_time = time.time()
    
    # Send the query to your custom API
    response_content = query({"question": prompt})
    
    # End the timer
    end_time = time.time()
    response_time = end_time - start_time  # Calculate the response time in seconds

    # Clear the thinking message after receiving the response
    thinking_placeholder.empty()

    # Display the assistant's response with the assistant avatar and response time
    with st.chat_message("assistant", avatar="https://github.com/Reese0301/GIS-AI-Agent/blob/main/4322991.png?raw=true"):
        st.markdown(f"💭 Thought for {response_time:.2f} seconds\n\n{response_content}")
    st.session_state.messages.append({"role": "assistant", "content": f"Thought for {response_time:.2f} seconds\n\n{response_content}"})

# Sidebar for suggested prompts or custom messages
with st.sidebar:
    st.markdown(
        """
        <div style="background-color: #f0f0f5; padding: 20px; border-radius: 10px;">
            <h4>💡 Suggested Prompts</h4>
            <ul>
                <li>What are the key steps to develop a career in investment banking?</li>
                <li>Surprise me with one insight on Investment Banking Recruiting.</li>
                <li>What are the dos and donts of a superday interview?</li>
                <li>Can you suggest networking strategies for international students? </li>
            </ul>
            <div style="margin-top: 20px; border-top: 1px solid #ccc; padding-top: 10px; text-align: center;">
                <small>For Feedback or Concerns, contact: <a href="mailto:yizhuoyang@hotmail.com">yizhuoyang@hotmail.com</a></small>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
