import requests
import streamlit as st


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
