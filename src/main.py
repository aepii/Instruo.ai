"""
1) python-pptx to extract slide topics and key points oand pymupdf for pdf extraction
2) openai to expand content
3) transfomers to use pipeline for cohesiveness
4) tts 
5) assemble visuals using moviepy
6) deploy as a webapp for ease of use (flask)
"""

import fitz
from language_model import prompt

def main():
    pdf = fitz.open("src/presentations/W6-L9-authentication.pdf")
    print(pdf.metadata)
    print(f"Total Pages: {pdf.page_count}")

    with open("src/output/output.txt", "w") as file:
        for index in range(pdf.page_count):
            page = pdf[index]
            text = page.get_text()
            next_text = pdf[index + 1].get_text() if index + 1 < pdf.page_count else None
            
            print(f"Page Number: {index + 1}\n{text}\n")
            prompt_text = prompt(text, next_text)

            file.write(f"Slide {index + 1}:\n{prompt_text}\n\n")

            if index == 4: 
                break

if __name__ == "__main__":
    main()