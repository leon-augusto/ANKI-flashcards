from decks_builder.services import generate_audios


class CardBasicLevel:
    def __init__(self, card_front, card_back, new_word, translated_word, language):
        self.card_front = card_front
        self.card_back = card_back
        self.new_word = new_word
        self.translated_word = translated_word
        self.audio = generate_audios(phrases=self.card_front, language=language)


class CardIntermediaryLevel:
    def __init__(self, card_front, new_word, pron_fon_w, context, translated_word, language):
        self.card_front = card_front
        self.new_word = new_word
        self.pron_fon_w = pron_fon_w
        self.context = context
        self.translated_word = translated_word
        self.card_back = []
        self.audio = generate_audios(phrases=self.card_front, language=language)


class CardAdvancedLevel:
    pass
