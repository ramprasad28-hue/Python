import streamlit as s
from google import genai
from google.genai import types
import  speech_recognition as sr
ch=genai.Client(api_key="AIzaSyCsW5FnkcFSPM3RCIjQ-m7i9o9ScCmR80Q")

s.title("ChatBot")
n=s.text_input("Ask anything")
##s.image("cheat.png")
##myimg=ch.files.upload(file="cheat.png")

if s.button("Record"):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        s.write("say..")
        audio=r.listen(source)

    text=r.recognize_google(audio)
    response=ch.models.generate_content(
        model="gemini-1.5-flash",
            contents=text
            )
    
    s.write(response.text)


if s.button("Ask"):
     response=ch.models.generate_content(
        model="gemini-1.5-flash",
            contents=n
            )
     
     s.write(response.text)
     
