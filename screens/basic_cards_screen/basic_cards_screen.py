from kivymd.uix.screen import MDScreen

from functions.creates import create_basic_cards


class BasicCardsScreen(MDScreen):
    def gen_basic_cards(self):
        lang = self.ids.lang.text
        create_basic_cards(lang)
