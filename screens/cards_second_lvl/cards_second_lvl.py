from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from decks_builder.views import create_intermediary_cards
import json


class CardsSecondLevelScreen(MDScreen):
    def gen_intermediary_cards(self):
        lang = self.ids.lang.text
        create_intermediary_cards(lang)

    def load_langs(self, *args):
        try:
            with open(MDApp.get_running_app().user_data_dir+'/builder-deck-langs.json','r') as data:
                return json.load(data)
        except FileNotFoundError:
            pass
