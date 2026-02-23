import streamlit as st
from chat import ask_question

st.set_page_config(page_title="Global ETF Intelligence Chatbot")

st.title("Global ETF Intelligence Chatbot")
st.caption("Educational use only – No investment advice")

question = st.text_input("Ask a question about ETFs:")

if question:
    with st.spinner("Searching documents..."):
        answer = ask_question(question)
        st.write(answer)
