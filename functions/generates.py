import genanki
import gtts


def genereteaudios(phrases, language):
    filesmp3 = []
    for phrase in phrases:
        texttospeech = gtts.gTTS(phrase, lang=language)
        filename = phrase.replace('.', '').lower().replace(' ', '-')[:] + '.mp3'
        texttospeech.save(filename)
        filesmp3.append(filename)
    return filesmp3


def genereteapkg(deck):
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

    genanki.Package(my_deck).write_to_file('my-new-cards.apkg')
