import pandas as pd

from classes import CardBasicLevel, CardIntermediaryLevel
from functions.generates import gen_apkg
from functions.intermediates import struturecard


def create_basic_cards(language):
    df = pd.read_excel('Basic-Intermediary-Advanced.xlsx', sheet_name='Basic')

    frontcard = df['ORIGINAL PHRASE']
    backcard = df['TRANSLATED SENTENCE']
    newword = df['NEW ORIGINAL WORD']
    translatedword = df['TRANSLATED WORD']

    objeto = CardBasicLevel(frontcard, backcard, newword, translatedword, language)
    deck = struturecard(level='basic', components=objeto)
    gen_apkg(deck)


def create_intermediary_cards(language):
    df = pd.read_excel('Basic-Intermediary-Advanced.xlsx', sheet_name='Intermediary')

    frontcard = df['PHRASE']
    newword = df['NEW WORD']
    pron_fon_w = df['WORD IN PHONETICS']
    sentido = df['CONTEXT']
    translatedword = df['TRANSLATED WORD']

    objeto = CardIntermediaryLevel(frontcard, newword, pron_fon_w, sentido, translatedword, language)
    deck = struturecard(level='intermediary', components=objeto)
    gen_apkg(deck)


def create_advanced_cards():
    pass
