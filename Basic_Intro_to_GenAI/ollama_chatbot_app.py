"""
ollama_chatbot_app.py
=====================
A chatbot web app built with Streamlit and Ollama.
Runs completely on your laptop — no internet or API key needed!

HOW TO RUN:
    1. Make sure Ollama is installed and running
       Download from: https://ollama.com
    2. Make sure you have downloaded a model:
           ollama pull llama3.2
    3. Open a terminal in this folder and run:
           streamlit run ollama_chatbot_app.py
    4. Your browser will open automatically with the chatbot!

REQUIREMENTS:
    pip install streamlit ollama
"""

import streamlit as st  # Streamlit creates the web interface
import ollama           # Ollama talks to the AI model on your laptop

# ================================================================
# CONFIGURATION — Change these to customise your chatbot!
# ================================================================

# The name shown in the browser tab and page title
CHATBOT_NAME = "Msaidizi Wangu"

# The subtitle shown under the title
CHATBOT_SUBTITLE = "Powered by Ollama | Running on your laptop — no internet needed!"

# The AI model to use (must be downloaded via: ollama pull <model-name>)
# Options: llama3.2, llama3.2:1b, gemma2, mistral, deepseek-r1
AI_MODEL = "llama3.2"

# The system message — this defines the AI's name, personality, and role.
# Change this to give the chatbot a different purpose!
SYSTEM_MESSAGE = """
You are Msaidizi, a friendly and helpful AI assistant for Kenyan secondary school students.
You explain things clearly using simple language and examples from everyday Kenyan life.
You are encouraging, patient, and supportive.
Keep your answers clear and concise.
"""

# Your name (shown in the sidebar as the developer)
DEVELOPER_NAME = "Your Name Here"

# ================================================================
# PAGE SETUP
# ================================================================

# Configure the Streamlit page
st.set_page_config(
    page_title=CHATBOT_NAME,   # browser tab title
    page_icon="🤖",            # browser tab icon
    layout="centered"          # layout style
)

# Page title and subtitle
st.title(f"🤖 {CHATBOT_NAME}")
st.caption(CHATBOT_SUBTITLE)

# ================================================================
# SIDEBAR
# ================================================================

# The sidebar appears on the left side of the page
with st.sidebar:
    st.header("About This Chatbot")
    st.write(f"**Name:** {CHATBOT_NAME}")
    st.write(f"**Model:** {AI_MODEL}")
    st.write(f"**Developer:** {DEVELOPER_NAME}")

    st.divider()  # a horizontal line

    st.header("How to Use")
    st.write("1. Type your question in the box at the bottom")
    st.write("2. Press **Enter** to send")
    st.write("3. Wait for the AI to reply")

    st.divider()

    # Clear Chat button — resets the conversation
    if st.button("🗑️ Clear Chat", use_container_width=True):
        # Reset the conversation history to just the system message
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_MESSAGE}
        ]
        st.rerun()  # refresh the page to show the cleared chat

# ================================================================
# CONVERSATION HISTORY (Memory)
# ================================================================

# st.session_state is Streamlit's way of remembering data between interactions
# We use it to store the full conversation history

# If this is the first time loading, create the messages list
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_MESSAGE}
    ]

# ================================================================
# DISPLAY PAST MESSAGES
# ================================================================

# Loop through the conversation history and show each message
for msg in st.session_state.messages:

    # Skip the system message — we don't show it to the user
    if msg["role"] == "system":
        continue

    # Show each message in a chat bubble (user or assistant style)
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ================================================================
# HANDLE NEW USER INPUT
# ================================================================

# st.chat_input creates the message box at the bottom of the page
user_input = st.chat_input("Type your message here...")

if user_input:  # only runs when the user has typed something and pressed Enter

    # 1. Show the user's message in the chat immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Add the user's message to the conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 3. Send the full conversation to Ollama and get a reply
    with st.chat_message("assistant"):
        # st.spinner shows a loading message while we wait for the AI
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model=AI_MODEL,
                messages=st.session_state.messages  # send full history
            )
            ai_reply = response["message"]["content"]

        # 4. Display the AI's reply
        st.markdown(ai_reply)

    ## 5. Add the AI's reply to history so the AI 'remembers' it next time
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
