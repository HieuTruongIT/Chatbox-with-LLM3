from langchain_community.llms import Ollama
import streamlit as st

llm = Ollama(model="gemma2")  # Chọn mô hình phù hợp

st.title("Chatbot using Ollama")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write_stream(llm.stream(prompt, stop=['<|eot_id|>']))
