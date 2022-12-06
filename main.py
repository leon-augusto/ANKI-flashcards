from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from custumizados import CustumButton

import contentfunctions


class Gerenciador(ScreenManager):
    pass

class PanelPrincipal(Screen):
    def gen_basic_cards(self):
        lang = self.ids.lang.text
        contentfunctions.content_basic_cards(lang)

    def gen_intermediary_cards(self):
        lang = self.ids.lang.text
        contentfunctions.content_intermediary_cards(lang)

    def gen_advanced_cards(self):
        pass


class Test(App):
    def build(self):
        return Gerenciador()


Test().run()
