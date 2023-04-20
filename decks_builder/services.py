import dragonmapper
from dragonmapper import hanzi
import genanki
import gtts
from datetime import datetime
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def define_cards(level, components):
    cards = []

    if level == 'basic':
        for i in range(0, len(components.card_front)):
            if components.new_word[i] in components.card_front[i]:
                components.card_front[i] = components.card_front[i].replace(components.new_word[i],
                                                                          f'<b>{components.new_word[i]}</b>')

            components.card_front[i] += '<div>[sound:' + components.audio[i] + ']</div>'

            if components.translated_word[i] in components.card_back[i]:
                components.card_back[i] = components.card_back[i].replace(components.translated_word[i],
                                                                        f'<b>{components.translated_word[i]}</b>')
        cards.append(components.card_front)
        cards.append(components.card_back)

    if level == 'intermediary':
        for i in range(0, len(components.card_front)):
            if components.new_word[i] in components.card_front[i]:
                components.card_front[i] = components.card_front[i].replace(components.new_word[i],
                                                                          f'<b>{components.new_word[i]}</b>')

            components.card_front[i] += '<div>[sound:' + components.audio[i] + ']</div>'
            components.card_back.append(f'<b>{components.new_word[i]} {components.pron_fon_w[i]}</b><br>'
                                       f'{components.context[i]} {components.translated_word[i]}')
        cards.append(components.card_front)
        cards.append(components.card_back)

    if level == 'advanced':
        pass

    return cards


def generate_filename(base, lang, extension):
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

        filename = base.replace(' ', '-').lower()
        filename += extension
    else:
        for character in special_chars:
            if character in base:
                base = base.replace(character, '')
        filename = base.replace(' ', '-').lower()
        filename += extension

    return filename


def generate_audios(phrases, language):
    files = []
    for phrase in phrases:
        speech = gtts.gTTS(phrase, lang=language)
        filename = generate_filename(base=phrase, lang=language, extension='.mp3')
        speech.save(os.path.join(BASE_DIR, 'assets', 'audios', filename))
        files.append(filename)
    return files


def generate_apkg(deck):
    front = deck[0]
    verse = deck[1]

    deck_to_anki = genanki.Deck(2059400110, 'My New Cards')

    model = genanki.Model(
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
        note = genanki.Note(model=model, fields=[front[i], verse[i]])
        deck_to_anki.add_note(note)

    genanki.Package(deck_to_anki).write_to_file(f'my-new-cards_{datetime.today()}.apkg'.replace(' ', '_'))


def move_audios():
    current_address = os.path.join(BASE_DIR, 'assets', 'audios')

    audio_list = os.listdir(current_address)

    for audio in audio_list:
        if '.mp3' in audio:
            os.rename(f'{current_address}/{audio}', f'/home/leon/Música/{audio}')

def move_apkg():
    current_address = BASE_DIR

    apkg_list = os.listdir(current_address)

    for apkg in apkg_list:
        if '.apkg' in apkg:
            os.rename(f'{current_address}/{apkg}', f'/home/leon/{apkg}')
