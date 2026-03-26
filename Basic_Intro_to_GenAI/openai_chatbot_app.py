"""
openai_chatbot_app.py
=====================
A chatbot web app built with Streamlit and OpenAI's GPT.
Requires an internet connection and an OpenAI API key.

HOW TO RUN:
    1. Get your API key from: https://platform.openai.com/api-keys
    2. Paste your API key in the OPENAI_API_KEY variable below
    3. Open a terminal in this folder and run:
           streamlit run openai_chatbot_app.py
    4. Your browser will open with the chatbot!

REQUIREMENTS:
    pip install streamlit openai

IMPORTANT:
    - NEVER share your API key with anyone!
    - Each conversation uses a small amount of API credits.
    - For free practice, use ollama_chatbot_app.py instead!
"""

import streamlit as st          # Streamlit creates the web interface
from openai import OpenAI       # OpenAI library to talk to GPT

# ================================================================
# CONFIGURATION — Change these to customise your chatbot!
# ================================================================

# IMPORTANT: Paste your OpenAI API key here
# Get one at: https://platform.openai.com/api-keys
OPENAI_API_KEY = "sk-your-api-key-here"   # <-- replace with your real key!

# The chatbot's display name
CHATBOT_NAME = "Kamau AI"

# The subtitle
CHATBOT_SUBTITLE = "Powered by OpenAI GPT | Requires internet connection"

# The GPT model to use
# 'gpt-4o-mini' is affordable and fast — great for students
AI_MODEL = "gpt-4o-mini"

# The system message — defines the AI's personality
SYSTEM_MESSAGE = """
You are Kamau, a friendly and helpful AI assistant for Kenyan secondary school students.
You explain things clearly using simple language and examples from everyday Kenyan life.
You are encouraging, patient, and supportive.
Keep your answers clear and concise.
"""

# Your name (shown in the sidebar)
DEVELOPER_NAME = "Your Name Here"

# ================================================================
# PAGE SETUP
# ================================================================

st.set_page_config(
    page_title=CHATBOT_NAME,
    page_icon="🤖",
    layout="centered"
)

st.title(f"🤖 {CHATBOT_NAME}")
st.caption(CHATBOT_SUBTITLE)

# ================================================================
# SIDEBAR
# ================================================================

with st.sidebar:
    st.header("About This Chatbot")
    st.write(f"**Name:** {CHATBOT_NAME}")
    st.write(f"**Model:** {AI_MODEL}")
    st.write(f"**Developer:** {DEVELOPER_NAME}")

    st.divider()

    st.header("How to Use")
    st.write("1. Type your question in the box at the bottom")
    st.write("2. Press **Enter** to send")
    st.write("3. Wait for the AI to reply")

    st.divider()

    # Show a warning about API costs
    st.warning("⚠️ This chatbot uses the OpenAI API which has small costs per message. Use Ollama for free practice!")

    st.divider()

    # Clear Chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_MESSAGE}
        ]
        st.rerun()

# ================================================================
# OPENAI CLIENT
# ================================================================

# Create the OpenAI client — the 'bridge' to OpenAI's servers
client = OpenAI(api_key=OPENAI_API_KEY)

# ================================================================
# CONVERSATION HISTORY (Memory)
# ================================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_MESSAGE}
    ]

# ================================================================
# DISPLAY PAST MESSAGES
# ================================================================

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ================================================================
# HANDLE NEW USER INPUT
# ================================================================

user_input = st.chat_input("Type your message here...")

if user_input:

    # Show user's message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get reply from OpenAI
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model=AI_MODEL,
                messages=st.session_state.messages
            )
            ai_reply = response.choices[0].message.content

        # Display the reply
        st.markdown(ai_reply)

    ## Save to history
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
