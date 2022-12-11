from functions.generates import genereteaudios


class CardBasicLevel:
    def __init__(self, frontcard, backcard, newword, translatedword, language):
        self.frontcard = frontcard
        self.backcard = backcard
        self.newword = newword
        self.translatedword = translatedword
        self.audio = genereteaudios(phrases=self.frontcard, language=language)


class CardIntermediaryLevel:
    def __init__(self, frontcard, newword, pron_fon_w, sentido, translatedword, language):
        self.frontcard = frontcard
        self.newword = newword
        self.pron_fon_w = pron_fon_w
        self.sentido = sentido
        self.translatedword = translatedword
        self.backcard = []
        self.audio = genereteaudios(phrases=self.frontcard, language=language)


class CardAdvancedLevel:
    pass
