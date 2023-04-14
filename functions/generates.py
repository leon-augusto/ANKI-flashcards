import dragonmapper
from dragonmapper import hanzi
import genanki
import gtts
from datetime import datetime
from pathlib import Path
import os

def gen_filename(base, lang, extension):
    base = base
    special_chars = ['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '_', '+', '=', '§', '/', '?', '°', '®', 'ŧ', '←',
                     '↓', '→', 'ø', 'þ', '`', '´', '{', '[', 'ª', '}', ']', 'º', '~', '^', ';', ':', '>', '.', '<', ',',
                     'µ', '”', '“', '©', '»', '«', 'æ', 'ß', 'ð', 'đ', 'ŋ', 'ħ', 'ˀ', 'ĸ', 'ł', 'ˇ', '\ ', '|', '+',
                     '-', '*', '/', '"']

    if lang == 'zh-CN':
        if dragonmapper.hanzi.is_simplified(base):
            base = dragonmapper.hanzi.to_pinyin(base)
            special_chars += ['“', '”', '=', '、', '：', '；', '？', '！', '。']
            accented_vowels = {'a': ['ā', 'á', 'ǎ', 'à',],
                               'e': ['ē', 'é', 'ě', 'è',],
                               'i': ['ī', 'í', 'ǐ', 'ì',],
                               'o': ['ō', 'ó', 'ǒ', 'ò',],
                               'u': ['ū', 'ú', 'ǔ', 'ù', 'ü']}

            for character in special_chars:
                if character in base:
                    base = base.replace(character, '')

            for vowel in accented_vowels:
                for character in accented_vowels[vowel]:
                    if character in base:
                        base = base.replace(character, vowel)

        base = base.replace(' ', '-').lower()
        base += extension
    else:
        for character in special_chars:
            if character in base:
                base = base.replace(character, '')
        base = base.replace(' ', '-').lower()
        base += extension

    return base

BASE_DIR = Path(__file__).resolve().parent.parent

def gen_audios(phrases, language):
    files = []
    for phrase in phrases:
        speech = gtts.gTTS(phrase, lang=language)
        filename = gen_filename(base=phrase, lang=language, extension='.mp3')
        speech.save(os.path.join(BASE_DIR, 'media', 'listening', filename))
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
    print(gen_filename('"我是Leon。"', 'zh-CN', '.mp3'))
