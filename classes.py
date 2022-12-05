import generateapkg
import texttospeech


class Card_Level_Basic:
    deck = []
    list_audios = []

    def __init__(self, front_card, back_card, new_word, tradu_word, language):
        self.front_card = front_card
        self.back_card = back_card
        self.new_word = new_word
        self.tradu_word = tradu_word
        self.list_audios = texttospeech.gen_audios(phrases=self.front_card, language=language)

    def preparar_cards(self):
        for i in range(0, len(self.front_card)):
            if self.new_word[i] in self.front_card[i]:
                self.front_card[i] = self.front_card[i].replace(self.new_word[i], f'<b>{self.new_word[i]}</b>')

            self.front_card[i] += '<div>[sound:' + self.list_audios[i] + ']</div>'

            if self.tradu_word[i] in self.back_card[i]:
                self.back_card[i] = self.back_card[i].replace(self.tradu_word[i], f'<b>{self.tradu_word[i]}</b>')

        self.deck.append(self.front_card)
        self.deck.append(self.back_card)
        generateapkg.gen_deck(self.deck)

class Card_Level_Intermediary:
    deck = []
    list_audios = []

    def __init__(self, front_card, new_word, pron_fon_w, sentido, tradu_word, language):
        self.front_card = front_card
        self.new_word = new_word
        self.pron_fon_w = pron_fon_w
        self.sentido = sentido
        self.tradu_word = tradu_word
        self.back_card = []
        self.list_audios = texttospeech.gen_audios(phrases=self.front_card, language=language)

    def preparar_cards(self):
        for i in range(0, len(self.front_card)):
            if self.new_word[i] in self.front_card[i]:
                self.front_card[i] = self.front_card[i].replace(self.new_word[i], f'<b>{self.new_word[i]}</b>')

            self.front_card[i] += '<div>[sound:'+self.list_audios[i]+']</div>'
            self.back_card.append(f'<b>{self.new_word[i]} {self.pron_fon_w[i]}</b><br>{self.sentido[i]} {self.tradu_word[i]}')

        self.deck.append(self.front_card)
        self.deck.append(self.back_card)
        generateapkg.gen_deck(self.deck)

class Card_Level_Advanced:
    pass
