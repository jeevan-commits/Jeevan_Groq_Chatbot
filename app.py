import streamlit as st
from groq import Groq


# -----------------------------
# Page Settings
# -----------------------------
st.set_page_config(
    page_title="Jeevan's Groq Chatbot",
    page_icon="🤖"
)


# -----------------------------
# Groq API Key
# -----------------------------
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)


# -----------------------------
# Title
# -----------------------------
st.title("🤖 Jeevan's Groq AI Chatbot")
st.write("Chat with an AI assistant powered by Groq.")


# -----------------------------
# Conversation History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful and friendly AI assistant."
        }
    ]


# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.write(message["content"])


# -----------------------------
# User Input
# -----------------------------
user_message = st.chat_input("Type your message here...")


# -----------------------------
# Send Message to Groq
# -----------------------------
if user_message:

    with st.chat_message("user"):
        st.write(user_message)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=st.session_state.messages
        )

        assistant_message = response.choices[0].message.content

        with st.chat_message("assistant"):
            st.write(assistant_message)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_message
            }
        )

    except Exception as e:

        st.error("❌ Groq API Error")
        st.write(str(e))