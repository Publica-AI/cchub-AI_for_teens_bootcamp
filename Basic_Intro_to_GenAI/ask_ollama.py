"""
ask_ollama.py
=============
A simple Python script to ask Ollama a question from the terminal.

HOW TO RUN:
    1. Make sure Ollama is installed and running on your laptop
    2. Make sure you have downloaded a model:
           ollama pull llama3.2
    3. Open a terminal in this folder and run:
           python ask_ollama.py

REQUIREMENTS:
    pip install ollama
"""

import ollama  # import the Ollama library

# ----------------------------------------------------------------
# Step 1: Choose your AI model
# ----------------------------------------------------------------
# Make sure you have downloaded this model first with:
#   ollama pull llama3.2
# For older/slower laptops, try: llama3.2:1b
MODEL = "llama3.2"

# ----------------------------------------------------------------
# Step 2: Give the AI a personality (system message)
# ----------------------------------------------------------------
# This tells the AI how to behave.
# You can change this to anything you want!
SYSTEM_MESSAGE = """
You are Amina, a friendly AI assistant for Kenyan secondary school students.
You explain things clearly using examples from everyday Kenyan life.
Keep your answers short, friendly, and easy to understand.
"""

# ----------------------------------------------------------------
# Step 3: Start the chat loop
# ----------------------------------------------------------------
def main():
    print("=" * 55)
    print("  🤖 Karibu! Welcome to Amina — Your AI Assistant")
    print("  Powered by Ollama | Running on your laptop!")
    print("=" * 55)
    print("  Type your question and press Enter.")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 55)
    print()

    # This list stores the full conversation history
    # We start with the system message so the AI knows its role
    conversation = [
        {"role": "system", "content": SYSTEM_MESSAGE}
    ]

    # Keep chatting until the user types 'bye' or 'exit'
    while True:
        # Get input from the user
        user_input = input("You: ").strip()

        # Check if the user wants to quit
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("\nAmina: Kwaheri! Goodbye — good luck with your studies! 👋")
            break

        # Skip empty inputs
        if not user_input:
            continue

        # Add the user's message to the conversation history
        conversation.append({"role": "user", "content": user_input})

        # Send the whole conversation to Ollama and get a reply
        print("\nAmina: ", end="", flush=True)
        response = ollama.chat(model=MODEL, messages=conversation)

        # Extract the AI's reply text
        ai_reply = response["message"]["content"]

        # Print the AI's reply
        print(ai_reply)
        print()

        # Add the AI's reply to history so it 'remembers' it next time
        conversation.append({"role": "assistant", "content": ai_reply})


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
