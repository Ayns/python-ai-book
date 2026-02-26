# Chapter 13 - Exercise Solutions
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Chatbot with mood detection
def chat_with_mood(user_message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Start each response by detecting the user's mood (happy, frustrated, curious, neutral) in brackets, then respond appropriately."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content

# 2. Conversation with memory (history)
def chat_with_history():
    history = [
        {"role": "system", "content": "You are a helpful Python tutor."}
    ]
    print("Chat with AI (type 'quit' to exit)")
    while True:
        user = input("You: ")
        if user.lower() == "quit":
            break
        history.append({"role": "user", "content": user})
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=history,
            max_tokens=300
        )
        reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        print(f"AI: {reply}\n")

# Uncomment to run:
# print(chat_with_mood("I can't figure out this bug and I'm so frustrated!"))
# chat_with_history()
