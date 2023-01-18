import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory


class HotReloader(MDApp, App):

    DEBUG = 1

    KV_FILES = {
        os.path.join(os.getcwd(), 'screens/screen_manager.kv'),
        os.path.join(os.getcwd(), 'screens/menu/menu.kv'),
        os.path.join(os.getcwd(), 'screens/cards_first_lvl/cards_first_lvl.kv'),
        os.path.join(os.getcwd(), 'screens/cards_second_lvl/cards_second_lvl.kv'),
        os.path.join(os.getcwd(), 'screens/languages/languages.kv'),

    }

    CLASSES = {
        'Manager': 'screens.screen_manager',
        'MenuScreen': 'screens.menu.menu',
        'CardsFirstLevelScreen': 'screens.cards_first_lvl.cards_first_lvl',
        'CardsSecondLevelScreen': 'screens.cards_second_lvl.cards_second_lvl',
        'DataFrameScreen': 'screens.dataframe.dataframe',
        'LanguagesScreen': 'screens.languages.languages',
    }

    AUTORELOADER_PATHS = [
        ('.', {'recursive': True}),
    ]

    def build_app(self):
        return Factory.Manager()

    def theme_dark(self):
        self.theme_cls.theme_style = 'Dark'

    def theme_light(self):
        self.theme_cls.theme_style = 'Light'


if __name__ == '__main__':
    HotReloader().run()
