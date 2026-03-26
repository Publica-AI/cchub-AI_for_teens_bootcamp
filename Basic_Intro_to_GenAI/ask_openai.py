"""
ask_openai.py
=============
A simple Python script to ask OpenAI's GPT a question from the terminal.

HOW TO RUN:
    1. Get your API key from: https://platform.openai.com/api-keys
    2. Paste your API key in the OPENAI_API_KEY variable below
    3. Open a terminal in this folder and run:
           python ask_openai.py

REQUIREMENTS:
    pip install openai

IMPORTANT:
    - NEVER share your API key with anyone!
    - Treat it like your M-PESA PIN — keep it private.
    - Each question costs a small amount from your API credits.
"""

from openai import OpenAI  # import the OpenAI library

# ----------------------------------------------------------------
# Step 1: Set your API key
# ----------------------------------------------------------------
# Paste your OpenAI API key here (starts with "sk-...")
# Get one at: https://platform.openai.com/api-keys
OPENAI_API_KEY = "sk-your-api-key-here"   # <-- replace this with your real key

# ----------------------------------------------------------------
# Step 2: Choose your model
# ----------------------------------------------------------------
# 'gpt-4o-mini' is fast and affordable — great for students!
MODEL = "gpt-4o-mini"

# ----------------------------------------------------------------
# Step 3: Give the AI a personality (system message)
# ----------------------------------------------------------------
SYSTEM_MESSAGE = """
You are Kamau, a friendly AI assistant for Kenyan secondary school students.
You explain things clearly using examples from everyday Kenyan life.
Keep your answers short, friendly, and easy to understand.
"""

# ----------------------------------------------------------------
# Step 4: Start the chat loop
# ----------------------------------------------------------------
def main():
    # Create the OpenAI client (the bridge to OpenAI's servers)
    client = OpenAI(api_key=OPENAI_API_KEY)

    print("=" * 55)
    print("  🤖 Karibu! Welcome to Kamau — Your AI Assistant")
    print("  Powered by OpenAI | Requires internet connection")
    print("=" * 55)
    print("  Type your question and press Enter.")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 55)
    print()

    # This list stores the full conversation history
    conversation = [
        {"role": "system", "content": SYSTEM_MESSAGE}
    ]

    # Keep chatting until the user types 'bye' or 'exit'
    while True:
        # Get input from the user
        user_input = input("You: ").strip()

        # Check if the user wants to quit
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("\nKamau: Kwaheri! Goodbye — keep learning! 👋")
            break

        # Skip empty inputs
        if not user_input:
            continue

        # Add the user's message to the conversation history
        conversation.append({"role": "user", "content": user_input})

        # Send the conversation to OpenAI and get a reply
        print("\nKamau: ", end="", flush=True)
        response = client.chat.completions.create(
            model=MODEL,
            messages=conversation
        )

        # Extract the AI's reply
        ai_reply = response.choices[0].message.content

        # Print the reply
        print(ai_reply)
        print()

        # Add the AI's reply to history so the conversation continues naturally
        conversation.append({"role": "assistant", "content": ai_reply})


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
