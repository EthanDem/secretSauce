import requests
import streamlit as st

st.set_page_config(page_title="Secret Sauce", page_icon=":shushing_face:")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {
    visibility: hidden;
}
footer:after {
    content: 'made by nBrain';
    visibility: visible;
    display: block;
    position: relative;
    /* background-color: red; */
    padding: 5px;
    top: 2px;
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

url = "https://ethantest.icecube1513.repl.co/request"

text = st.text_input("Enter text")

if st.button("Magic"):
  
  params = {
      "text": text
  }
  
  response = requests.post(url, params=params)
  
  if response.status_code == 200:
      st.write("Response from server:", response.json())
  else:
      st.write("Error:", response.status_code, response.text)
