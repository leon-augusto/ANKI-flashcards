from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from custumizados import CustumButton

from functions.creates import create_basic_cards, create_intermediary_cards


class Gerenciador(ScreenManager):
    pass


class PanelPrincipal(Screen):
    def gen_basic_cards(self):
        lang = self.ids.lang.text
        create_basic_cards(lang)

    def gen_intermediary_cards(self):
        lang = self.ids.lang.text
        create_intermediary_cards(lang)

    def gen_advanced_cards(self):
        pass


class Test(App):
    def build(self):
        return Gerenciador()


Test().run()
