import os
import google.generativeai as genai

key = os.environ["API_KEY"]
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")

def prompt(current_text, next_text=None):
    transition_text = f" and be ready to transition into the next topic: {next_text}" if next_text else ""
    response = model.generate_content(
        f"Pretend you are explaining the following slide content as part of an educational video: {current_text}{transition_text}"
    )
    return response.text