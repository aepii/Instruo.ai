import re
import fitz
import textwrap
from language_model import prompt
from text_to_speech import speech

# Clean the text by removing unwanted symbols and extra whitespaces
def clean_text(text):
    text = re.sub(r"\*+", "", text)  # Remove all asterisks
    text = re.sub(r"Slide \d+:", "", text)  # Remove "Slide X:" labels
    text = re.sub(r"\n\s*\n", "\n", text)  # Remove extra blank lines
    text = text.strip()  # Remove leading/trailing whitespace
    return text

# Split the text into chunks to avoid exceeding the API limits (default max 4000 characters)
def split_text(text, max_length=4000):
    return textwrap.wrap(text, width=max_length)  # Split by max length

# Main function to process PDF and generate audio
def main():
    pdf = fitz.open("src/presentations/W6-L9-authentication.pdf")

    with open("src/output/output.txt", "w+") as file:
        for index, page in enumerate(pdf):
            text = page.get_text()
            next_text = pdf[index + 1].get_text() if index + 1 < pdf.page_count else None
            
            # Get the cleaned prompt for this page
            prompt_text = prompt(text, next_text)
            prompt_text = clean_text(prompt_text)

            file.write(f"{prompt_text}\n\n")

            # Split the cleaned prompt text into smaller chunks
            chunks = split_text(prompt_text)

            # Process each chunk individually
            for chunk_num, chunk in enumerate(chunks):
                # Generate speech for each chunk, passing chunk number to avoid overwriting
                print(index, chunk, chunk_num)
                speech(chunk, f"{index}-{chunk_num}") 

            if index == 4:  # Stop after 5 pages for testing, adjust as needed
                break

if __name__ == "__main__":
    main()