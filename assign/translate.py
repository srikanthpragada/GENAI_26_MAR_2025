import streamlit as st
from huggingface_hub import InferenceClient
import keys

model_id = "Helsinki-NLP/opus-mt-en-hi"   
client = InferenceClient(model=model_id, 
                         token= keys.HUGGINGFACE_KEY)

st.title("English to Hindi")
text  = st.text_input("English Text :", "")

if len(text) > 0:
    hindi = client.translation(text)
    st.write(hindi.translation_text)

     