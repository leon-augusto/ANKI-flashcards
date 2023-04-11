import genanki
import gtts
from datetime import datetime
from pathlib import Path
import os

def gen_filename(base, extension):
    name = base
    special_chars = ['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '_', '+', '=', '§', '/', '?', '°', '®', 'ŧ', '←', '↓', '→', 'ø', 'þ', '`', '´', '{', '[', 'ª', '}', ']', 'º', '~', '^', ';', ':', '>', '.', '<', ',', 'µ', '”', '“', '©', '»', '«', 'æ', 'ß', 'ð', 'đ', 'ŋ', 'ħ', 'ˀ', 'ĸ', 'ł', 'ˇ', '\ ', '|', '+', '-', '*', '/', '"']
    for character in special_chars:
        if character in name:
            name = name.replace(character, '')
    name = name.replace(' ', '-').lower()
    name += extension
    return name

BASE_DIR = Path(__file__).resolve().parent.parent

def gen_audios(phrases, language):
    files = []
    for phrase in phrases:
        speech = gtts.gTTS(phrase, lang=language)
        filename = gen_filename(base=phrase, extension='.mp3')
        speech.save(os.path.join(BASE_DIR, 'media', 'listening' + filename))
        files.append(filename)
    return files


def gen_apkg(deck):
    front = deck[0]
    verse = deck[1]

    my_deck = genanki.Deck(
        2059400110,
        'My New Cards')

    my_model = genanki.Model(
        1091735104,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
        css='.card {'
            '\n font-family: arial;'
            '\n font-size: 20px;'
            '\n text-align: center;'
            '\n color: black; background-color: white;'
            '\n}\n')

    for i in range(0, len(front)):
        my_note = genanki.Note(
            model=my_model,
            fields=[front[i], verse[i]])

        my_deck.add_note(my_note)

    genanki.Package(my_deck).write_to_file(f'my-new-cards_{datetime.today()}.apkg'.replace(' ', '_'))


if __name__ == '__main__':
    print(f'my-new-cards_{datetime.today()}.apkg'.replace(' ', '_'))
    print(gen_filename('"Hello, World!"', '.mp3'))