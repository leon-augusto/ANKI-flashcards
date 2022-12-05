import pandas as pd

import classes

def content_basic_cards(language):
    df = pd.read_excel('Basic-Intermediary-Advanced.xlsx', sheet_name='Basic')

    front_card = df['ORIGINAL PHRASE']
    back_card = df['TRANSLATED SENTENCE']
    new_word = df['NEW ORIGINAL WORD']
    tradu_word = df['TRANSLATED WORD']

    objeto = classes.Card_Level_Basic(front_card, back_card, new_word, tradu_word, language)
    objeto.preparar_cards()

def content_intermediary_cards(language):
    df = pd.read_excel('Basic-Intermediary-Advanced.xlsx', sheet_name='Intermediary')

    front_card = df['PHRASE']
    new_word = df['NEW WORD']
    pron_fon_w = df['WORD IN PHONETICS']
    sentido = df['CONTEXT']
    tradu_word = df['TRANSLATED WORD']

    objeto = classes.Card_Level_Intermediary(front_card, new_word, pron_fon_w, sentido, tradu_word, language)
    objeto.preparar_cards()

def content_advanced_cards():
    pass
