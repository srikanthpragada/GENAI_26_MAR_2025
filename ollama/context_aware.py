import streamlit as st
from langchain_ollama import OllamaLLM

MODEL_NAME = "llama3.2:1b"   
llm = OllamaLLM(model=MODEL_NAME)

st.set_page_config(page_title="LLaMA 3.2 Chatbot", layout="centered")
st.title("🤖 Chat with Local LLaMA 3.2 (via Ollama)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Ask something...")
st.button("Start New Chat", on_click=lambda: st.session_state.pop("messages", None))
if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare context as a single prompt for LLM
    history = "\n".join(
        [f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages]
    )
    full_prompt = history + "\nAssistant:"

    # Call Ollama
    with st.spinner("LLaMA is thinking..."):
        reply = llm.invoke(full_prompt)
      

    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)


 
         