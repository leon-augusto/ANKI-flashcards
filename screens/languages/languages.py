from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from gtts.langs import _langs
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineListItem
from kivy.core.window import Window
import json


class CustomTwoLineListItem(TwoLineListItem):

    def set_language(self):
        pass


class LanguagesScreen(MDScreen):
    languages = []
    path = ''

    def set_list_gtts_langs(self, text='', search=False):

        def add_icon_item(_lang_value, _lang_key):
            self.ids.rv.data.append(
                {
                    'viewclass': 'CustomTwoLineListItem',
                    'text': _lang_value,
                    'secondary_text': _lang_key,
                    'set_language': lambda x: {
                        self.close_list_gtts_langs(),
                        self.add_lang(_lang_key)
                    },
                }
            )

        self.ids.rv.data = []
        for _lang in _langs.keys():
            if search:
                if text.lower() in _langs.get(_lang).lower():
                    add_icon_item(_langs.get(_lang), _lang)
            else:
                add_icon_item(_langs.get(_lang), _lang)

    def close_list_gtts_langs(self):
        self.ids.rv.data = []
        self.ids.search_field.text = ''

    def on_pre_enter(self):
        self.ids.languages_box.clear_widgets()
        self.path = MDApp.get_running_app().user_data_dir+'/'
        self.load_data()
        Window.bind(on_keyboard=self.voltar)
        for language in self.languages:
            self.ids.languages_box.add_widget(Language(text=language))

    def voltar(self,window,key,*args):
        if key == 27:
            MDApp.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def load_data(self,*args):
        try:
            with open(self.path+'data.json','r') as data:
                self.languages = json.load(data)
        except FileNotFoundError:
            pass

    def save_data(self,*args):
        with open(self.path+'data.json','w') as data:
            json.dump(self.languages, data)

    def remove_lang(self, language):
        texto = language.ids.lang.text
        self.ids.languages_box.remove_widget(language)
        self.languages.remove(texto)
        self.save_data()

    def add_lang(self, lang):
        self.ids.languages_box.add_widget(Language(text=lang))
        self.languages.append(lang)
        self.save_data()


class Language(MDBoxLayout):
    def __init__(self, text='', **kwargs):
        super(Language, self).__init__(**kwargs)
        self.ids.lang.text = text
