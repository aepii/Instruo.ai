# Use the generative AI model to format the text
import google.generativeai as genai

genai.configure()
model = genai.GenerativeModel("gemini-1.5-flash")

def prompt(current_text, next_text=None):
    transition_text = f" and be ready to transition into the next topic: {next_text}" if next_text else ""
    response = model.generate_content(
        f"Convert the following slide notes into a natural, spoken transcript for an educational video. Ignore any symbols, headings, or slide markers: {current_text}{transition_text}"
    )
    return response.text