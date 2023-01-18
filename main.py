from kivymd.app import MDApp
from screens.screen_manager import Manager


class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)

    def build(self):
        return Manager()

    def theme_dark(self):
        self.theme_cls.theme_style = 'Dark'

    def theme_light(self):
        self.theme_cls.theme_style = 'Light'


if __name__ == '__main__':
    MainApp().run()
