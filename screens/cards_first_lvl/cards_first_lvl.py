from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from functions.creates import create_basic_cards
import json


class CardsFirstLevelScreen(MDScreen):
    def gen_basic_cards(self):
        lang = self.ids.lang.text
        create_basic_cards(lang)

    def load_langs(self, *args):
        try:
            with open(MDApp.get_running_app().user_data_dir+'/builder-deck-langs.json','r') as data:
                return json.load(data)
        except FileNotFoundError:
            pass
