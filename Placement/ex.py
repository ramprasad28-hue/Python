from google import genai
robo=genai.Client(api_key="AIzaSyCsW5FnkcFSPM3RCIjQ-m7i9o9ScCmR80Q")
response=robo.models.generate_content(
    model="gemini-1.5-flash",
    contents="tell about me")
print(response.text)
