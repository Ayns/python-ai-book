# AI Chatbot - Chapter 13

import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except openai.AuthenticationError:
        return "Error: Invalid API key. Check your .env file."
    except openai.RateLimitError:
        return "Error: Rate limited. Please wait a moment."
    except openai.APIError as err:
        return f"Error: {err}"


def main():
    print("=" * 40)
    print("   AI CHATBOT")
    print("=" * 40)
    print("Type 'quit' to exit.")
    print("Type 'clear' to start a new conversation.")
    print()

    messages = [
        {"role": "system", "content": "You are a helpful, friendly assistant. Keep responses concise but informative."}
    ]

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        if user_input.lower() == "clear":
            messages = [messages[0]]
            print("Conversation cleared.\n")
            continue

        messages.append({"role": "user", "content": user_input})
        reply = chat(messages)
        print(f"\nAI: {reply}\n")
        messages.append({"role": "assistant", "content": reply})


main()
