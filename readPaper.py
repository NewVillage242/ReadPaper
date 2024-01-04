from openai import OpenAI
import os
from dotenv import load_dotenv
from pathlib import Path

def text_to_speech(client, text, speech_file_path,model="tts-1", voice="nova"):
    try:
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )

        if speech_file_path.exists():
            speech_file_path.unlink()
            
        response.stream_to_file(speech_file_path)
        return speech_file_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

load_dotenv()
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

file_path = Path(os.getenv('INPUT')) / os.getenv('ARTICLE')
output_path=Path(os.getenv('OUTPUT')) / os.getenv('ARTICLE')
output_path.mkdir(parents=True, exist_ok=True)
files = os.listdir(Path(file_path) / "processed")

for subpath in files:
    with open(file_path/ "processed" / subpath,'r') as file:
        line = file.read()
        if os.path.exists(output_path/f"{subpath}.mp3") == False:
            print(f"processing file {subpath}")
            text_to_speech(client, line, output_path/f"{subpath}.mp3")
        else:
            print(f"{subpath} already exists.")