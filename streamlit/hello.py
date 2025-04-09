import streamlit as st

st.title("Demo")
name = st.text_input("Enter your name", "Srikanth")
st.write(f"Hello {name}, welcome to the Streamlit app!")
     