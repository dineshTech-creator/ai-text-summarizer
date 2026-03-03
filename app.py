import streamlit as st
from openai import OpenAI
import os

# Get API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Text Summarizer", page_icon="🤖")

st.title("🤖 AI Text Summarizer")
st.write("Summarize long text instantly using Generative AI.")

text = st.text_area("Enter your text here:", height=200)

if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": f"Summarize this text in 3 clear lines:\n{text}"}
                ]
            )
            summary = response.choices[0].message.content
            st.success("Summary Generated!")
            st.write(summary)