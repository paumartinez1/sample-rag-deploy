import streamlit as st
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

# Load OpenAI API key
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
#st.write(f'API Key: {openai_api_key}')


# For API Key, in case this is needed
#api_input_label = "Enter your OpenAI API key:"
#openai_api_key = st.sidebar.text_input(api_input_label, type="password", #placeholder="Your API key here")

title = "<h1 style='font-size:50px; color:white'>RAGxStreamlit Application</h1>"
st.markdown(title, unsafe_allow_html=True)
## Can also do; but difficult to modify:
# st.title('Title')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter your question:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
