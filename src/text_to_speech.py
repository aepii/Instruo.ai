# Google Cloud Text-to-Speech API function to generate audio from text
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Standard-F", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

def speech(prompt, id):
    # Create a synthesis input from the given prompt
    synthesis_input = texttospeech.SynthesisInput(text=prompt)
    
    # Get the speech response from Google Cloud Text-to-Speech
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # Save the resulting speech to a file, appending the chunk number to the filename
    with open(f"src/output/output_{id}.mp3", "wb") as out:
        out.write(response.audio_content)