from google import genai
from google.genai import types
ch=genai.Client(api_key="AIzaSyCsW5FnkcFSPM3RCIjQ-m7i9o9ScCmR80Q")
myimg=ch.files.upload(file="")
while True:
    qu=input("user: ")
    res=ch.models.generate_content(
        model="gemini-1.5-flash",
        config=types.GenerateContentConfig(
system_instruction="for any input respond "),
        contents=qu
        )
print("AI: ",res.text)
