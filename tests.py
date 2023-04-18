from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def move_audios():
    current_address = os.path.join(BASE_DIR, 'ANKI-flashcards', 'media', 'listening')

    audio_list = os.listdir(current_address)

    for audio in audio_list:
        if ".mp3" in audio:
            os.rename(f"{current_address}/{audio}", f"/home/leon/Música/{audio}")

def move_apkg():
    current_address = os.path.join(BASE_DIR, 'ANKI-flashcards')

    apkg_list = os.listdir(current_address)

    for apkg in apkg_list:
        if ".apkg" in apkg:
            os.rename(f"{current_address}/{apkg}", f"/home/leon/{apkg}")

def move_files():
    move_audios()
    move_apkg()


if __name__ == '__main__':
    move_files()

