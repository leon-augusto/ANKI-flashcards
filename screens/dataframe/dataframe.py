from kivymd.uix.screen import MDScreen
from plyer import filechooser


class DataFrameScreen(MDScreen):
    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            self.ids.selected_path.text = selection[0]