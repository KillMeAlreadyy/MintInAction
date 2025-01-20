import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Chatbot", layout="centered")

st.title("Chatbot")
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)
# Initialize session state to store the conversation
if "messages" not in st.session_state:
    st.session_state["messages"] = []

def generate_response(prompt, messages_so_far):
    """
    Generates a response from the model given the user prompt and conversation history.
    Replace this function with your own model or OpenAI API calls.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far + [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Chat interface
def chat_interface():
    # Input box for the user's prompt
    user_input = st.chat_input(key="user_input", placeholder="Type your question here...")

    # When the user hits Enter or clicks a button, generate a response.
    if user_input:
        if user_input.strip():
            # Add user query to the conversation history
            st.session_state["messages"].append({"role": "user", "content": user_input})

            # Generate a response
            response_text = generate_response(user_input, st.session_state["messages"])

            # Add the assistant response to the conversation history
            st.session_state["messages"].append({"role": "assistant", "content": response_text})

    # Display the conversation
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            st.markdown(f"**User**: {msg['content']}")
        else:
            st.markdown(f"**Assistant**: {msg['content']}")


if __name__ == "__main__":
    chat_interface()
