import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Groq Chat", page_icon="💬")

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

DEFAULT_ROLE = "helpful assistant"

# --- Session state setup ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "developer", "content": f"You are a {DEFAULT_ROLE}."}
    ]
if "role" not in st.session_state:
    st.session_state.role = DEFAULT_ROLE

# --- Sidebar: role switch ---
st.sidebar.title("Settings")
new_role = st.sidebar.text_input("Bot role", value=st.session_state.role)

if st.sidebar.button("Switch role"):
    st.session_state.role = new_role
    st.session_state.messages[0] = {
        "role": "developer",
        "content": f"You are a {new_role}."
    }
    st.sidebar.success(f"Switched to {new_role} mode.")

if st.sidebar.button("Clear chat"):
    st.session_state.messages = [
        {"role": "developer", "content": f"You are a {st.session_state.role}."}
    ]
    st.rerun()

st.title("💬 Groq Chat")

# --- Show chat history (skip the developer/system message) ---
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat input ---
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_reply = ""

        response = client.responses.create(
            model="openai/gpt-oss-120b",
            input=st.session_state.messages,
            stream=True
        )

        for event in response:
            if event.type == "response.output_text.delta":
                full_reply += event.delta
                placeholder.markdown(full_reply)

    st.session_state.messages.append({"role": "assistant", "content": full_reply})