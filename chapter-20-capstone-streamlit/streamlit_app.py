# AI-Powered Web App with Streamlit - Chapter 20 Capstone
# Requirements: pip install streamlit openai python-dotenv
# Run with: streamlit run streamlit_app.py

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import openai
import streamlit as st

load_dotenv()


def get_client():
    """Get OpenAI client with API key"""
    api_key = os.getenv("OPENAI_API_KEY") or st.session_state.get("api_key")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


def ask_ai(client, prompt, system="You are a helpful assistant.", temperature=0.7):
    """Send a prompt to the AI and return the response"""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content
    except openai.APIError as err:
        return f"Error: {err}"


# ─── Page Configuration ───
st.set_page_config(page_title="AI Dashboard", page_icon="🤖", layout="wide")

st.title("🤖 AI-Powered Dashboard")
st.markdown("Built with Python, OpenAI, and Streamlit — Chapter 20")

# ─── Sidebar: API Key ───
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("OpenAI API Key", type="password")
    if api_key:
        st.session_state["api_key"] = api_key
        st.success("API key set!")

    st.divider()
    st.markdown("**Tools:**")
    tool = st.radio("Choose a tool", [
        "💬 Chat",
        "📝 Summarizer",
        "🌐 Translator",
        "📊 Data Extractor"
    ])

client = get_client()
if not client:
    st.warning("Please enter your OpenAI API key in the sidebar.")
    st.stop()

# ─── Chat Tool ───
if tool == "💬 Chat":
    st.header("💬 AI Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            response = ask_ai(client, prompt)
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ─── Summarizer ───
elif tool == "📝 Summarizer":
    st.header("📝 Text Summarizer")
    text = st.text_area("Paste text to summarize", height=200)
    sentences = st.slider("Summary length (sentences)", 1, 10, 3)

    if st.button("Summarize") and text:
        with st.spinner("Summarizing..."):
            result = ask_ai(
                client,
                f"Summarize in {sentences} sentences:\n\n{text}",
                temperature=0.3
            )
        st.subheader("Summary")
        st.write(result)

# ─── Translator ───
elif tool == "🌐 Translator":
    st.header("🌐 Translator")
    text = st.text_area("Text to translate", height=150)
    target = st.selectbox("Target language", [
        "Spanish", "French", "German", "Japanese", "Hindi",
        "Tamil", "Chinese", "Korean", "Arabic", "Portuguese"
    ])

    if st.button("Translate") and text:
        with st.spinner("Translating..."):
            result = ask_ai(
                client,
                f"Translate to {target}. Return only the translation:\n\n{text}",
                temperature=0.3
            )
        st.subheader(f"Translation ({target})")
        st.write(result)

# ─── Data Extractor ───
elif tool == "📊 Data Extractor":
    st.header("📊 Data Extractor")
    text = st.text_area("Paste text to extract data from", height=200)

    if st.button("Extract") and text:
        with st.spinner("Extracting..."):
            result = ask_ai(
                client,
                f'Extract people, organizations, locations, and dates from this text. Return ONLY valid JSON: {{"people": [], "organizations": [], "locations": [], "dates": []}}\n\nText: {text}',
                temperature=0
            )
        try:
            data = json.loads(result)
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("People")
                for item in data.get("people", []):
                    st.write(f"• {item}")
                st.subheader("Locations")
                for item in data.get("locations", []):
                    st.write(f"• {item}")
            with col2:
                st.subheader("Organizations")
                for item in data.get("organizations", []):
                    st.write(f"• {item}")
                st.subheader("Dates")
                for item in data.get("dates", []):
                    st.write(f"• {item}")
        except json.JSONDecodeError:
            st.code(result)
