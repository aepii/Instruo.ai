import os
import google.generativeai as genai

key = os.environ["API_KEY"]
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)