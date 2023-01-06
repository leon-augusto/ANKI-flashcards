from kivymd.uix.screen import MDScreen

from functions.creates import create_intermediary_cards


class IntermediaryCardsScreen(MDScreen):
    def gen_intermediary_cards(self):
        lang = self.ids.lang.text
        create_intermediary_cards(lang)
