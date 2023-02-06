import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory


class GenFlashcards(MDApp, App):

    DEBUG = 1

    KV_FILES = {
        os.path.join(os.getcwd(), 'screens/screenmanager.kv'),
        os.path.join(os.getcwd(), 'screens/menu/menu.kv'),
        os.path.join(os.getcwd(), 'screens/basic_cards_screen/basic_cards_screen.kv'),
        os.path.join(os.getcwd(), 'screens/intermediary_cards_screen/intermediary_cards_screen.kv'),
        os.path.join(os.getcwd(), 'screens/dataframe/dataframe.kv'),

    }

    CLASSES = {
        'MainScreenManager': 'screens.screenmanager',
        'Menu': 'screens.menu.menu',
        'BasicCardsScreen': 'screens.basic_cards_screen.basic_cards_screen',
        'IntermediaryCardsScreen': 'screens.intermediary_cards_screen.intermediary_cards_screen',
        'DataFrameScreen': 'screens.dataframe.dataframe',
    }

    AUTORELOADER_PATHS = [
        ('.', {'recursive': True}),
    ]

    def build_app(self):
        return Factory.MainScreenManager()

    def theme_dark(self):
        self.theme_cls.theme_style = 'Dark'

    def theme_light(self):
        self.theme_cls.theme_style = 'Light'


if __name__ == '__main__':
    GenFlashcards().run()
