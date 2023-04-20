from decks_builder.models import CardBasicLevel, CardIntermediaryLevel
from decks_builder.services import define_cards, generate_apkg
import pandas as pd


def create_basic_cards(language):
    df = pd.read_excel('Basic-Intermediary-Advanced.xlsx', sheet_name='Basic')

    card_front = df['ORIGINAL PHRASE']
    card_back = df['TRANSLATED SENTENCE']
    new_word = df['NEW ORIGINAL WORD']
    translated_word = df['TRANSLATED WORD']

    components = CardBasicLevel(card_front, card_back, new_word, translated_word, language)
    deck = define_cards(level='basic', components=components)
    generate_apkg(deck)


def create_intermediary_cards(language):
    df = pd.read_excel('Basic-Intermediary-Advanced.xlsx', sheet_name='Intermediary')

    card_front = df['PHRASE']
    new_word = df['NEW WORD']
    pron_fon_w = df['WORD IN PHONETICS']
    context = df['CONTEXT']
    translated_word = df['TRANSLATED WORD']

    components = CardIntermediaryLevel(card_front, new_word, pron_fon_w, context, translated_word, language)
    deck = define_cards(level='intermediary', components=components)
    generate_apkg(deck)


def create_advanced_cards():
    pass
