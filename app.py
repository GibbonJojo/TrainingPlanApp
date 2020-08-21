# --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import re

from builder_string import BUILDER_STRING
from screens.strength import StrengthScreen
from screens.strengthmaintenance import StrengthMaintenanceScreen
from screens.power import PowerScreen
from screens.powermaintenance import PowerMaintenanceScreen
from screens.pe import PEScreen
from screens.pemaintenance import PEMaintenanceScreen
from screens.prehab import PrehabScreen

Builder.load_string(BUILDER_STRING)


class MenuScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(StrengthScreen(sm=sm, name='strength'))
sm.add_widget(StrengthMaintenanceScreen(name='strengthmain'))
sm.add_widget(PowerScreen(name='power'))
sm.add_widget(PowerMaintenanceScreen(name='powermain'))
sm.add_widget(PEScreen(name='pe'))
sm.add_widget(PEMaintenanceScreen(name='pemain'))
sm.add_widget(PrehabScreen(name='prehab'))


class Main(App):

    def build(self):
        return sm


if __name__ == '__main__':
    Main().run()





# class Main(GridLayout):
#
#     def __init__(self, **kwargs):
#         super(Main, self).__init__(**kwargs)
#         self.cols = 1
#         # self.moves_slider = Slider(min=0, max=5, value=3, value_track=True, step=1, value_track_color=[1,0,0,1])
#         # self.moves_label = Label(text=f"Moves ({str(self.moves_slider.value)})")
#         # self.add_widget(self.moves_label)
#         # self.moves_slider.bind(value=self.slider_value)
#         # self.add_widget(self.moves_slider)
#
#         maintenance_width = 160
#
#         strength_button = Button(text="Strength")
#         strength_m_button = Button(text="""
# Strength
# Maintenance""", size_hint_x=None, width=maintenance_width)
#         power_button = Button(text="Power")
#         power_m_button = Button(text="""
# Power
# Maintenance""", size_hint_x=None, width=maintenance_width)
#         pe_button = Button(text="Power Endurance")
#         pe_m_button = Button(text="""
# Power Endurance
# Maintenance""", size_hint_x=None, width=maintenance_width)
#
#         prehab_button = Button(text="Prehab")
#         antagonist_button = Button(text="Antagonist")
#
#         strength_grid = GridLayout(cols=2)
#         power_grid = GridLayout(cols=2)
#         pe_grid = GridLayout(cols=2)
#
#         strength_grid.add_widget(strength_button)
#         strength_grid.add_widget(strength_m_button)
#         power_grid.add_widget(power_button)
#         power_grid.add_widget(power_m_button)
#         pe_grid.add_widget(pe_button)
#         pe_grid.add_widget(pe_m_button)
#
#         self.add_widget(strength_grid)
#         self.add_widget(power_grid)
#         self.add_widget(pe_grid)
#         self.add_widget(antagonist_button)
#         self.add_widget(prehab_button)
#
#     def p(self, event):
#         grade = "White" if self.grade_check.active else ""
#         self.grade_text.text = grade
#
#         hold = "Sloper" if self.hold_check.active else ""
#         self.hold_text.text = hold
#
#         moves_list = ["Drop Knee", "Gaston", "Toe Hook", "Dyno", "Knee Bar"]
#         moves = moves_list[:int(self.moves_slider.value)]
#         self.moves_text.text = ", ".join(moves)
#
#     def slider_value(self, event, value):
#         self.moves_label.text = f"Moves ({int(value)})"
#
#
# class MyApp(App):
#
#     def build(self):
#         return Main()
#
#
# if __name__ == '__main__':
#     MyApp().run()
