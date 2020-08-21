from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class PrehabScreen(Screen):
    def __init__(self, **kwargs):
        super(PrehabScreen, self).__init__(**kwargs)
        self.grid = GridLayout()
        self.grid.cols = 1
        self.grid.add_widget(Button(text="Back"))

        self.add_widget(self.grid)