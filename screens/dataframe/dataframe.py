from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from plyer import filechooser
import json


class DataFrameScreen(MDScreen):
    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            self.ids.selected_path.text = selection[0]
            with open(MDApp.get_running_app().user_data_dir + '/builder-deck-df-address.json', 'w') as data:
                json.dump(selection[0], data)

    def get_dataframe_address(self, *args):
        try:
            with open(MDApp.get_running_app().user_data_dir+'/builder-deck-df-address.json','r') as data:
                return json.load(data)
        except FileNotFoundError:
            return 'File not selected...'
