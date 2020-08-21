from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from server import Server

from helper.numberinput import NumberInput


class StrengthScreen(Screen):
    def __init__(self, sm, **kwargs):
        self.sm = sm
        super(StrengthScreen, self).__init__(**kwargs)
        self.main_grid = GridLayout(cols=1)
        back_button = Button(text="Back")
        back_button.bind(on_press=self.to_main)

        self.main_grid.add_widget(back_button)

        self.create_hangboard()
        self.create_weighted_pu()

        self.add_widget(self.main_grid)

    def create_hangboard(self):

        self.main_grid.add_widget(Label(text="Hangboard"))
        pu_grid = GridLayout(cols=5)
        labels = {x: Label(text=x.capitalize()) for x in ["hang", "sets", "rest", "weight"]}
        for k in labels:
            pu_grid.add_widget(labels[k])
        pu_grid.add_widget(Label())

        inputs = {
            "hang": NumberInput(text="10"),
            "sets": NumberInput(text="5"),
            "rest": NumberInput(text="180"),
            "weight": NumberInput(),
        }
        for k in inputs:
            pu_grid.add_widget(inputs[k])
        submit = Button(text="Submit")

        submit.bind(on_press=lambda x: self.post("hangboard", inputs))
        pu_grid.add_widget(submit)

        self.main_grid.add_widget(pu_grid)

    def create_weighted_pu(self):
        self.main_grid.add_widget(Label(text="Weighted Pull-Ups"))
        hang_grid = GridLayout(cols=5)
        hang_grid.add_widget(Label(text="Reps"))
        hang_grid.add_widget(Label(text="Sets"))
        hang_grid.add_widget(Label(text="Pause"))
        hang_grid.add_widget(Label(text="Weight"))
        hang_grid.add_widget(Label())
        hang_grid.add_widget(NumberInput())
        hang_grid.add_widget(NumberInput())
        hang_grid.add_widget(NumberInput())
        hang_grid.add_widget(NumberInput())

        submit = Button(text="Submit")
        submit.bind(on_press=lambda x: print("Done"))
        hang_grid.add_widget(submit)

        self.main_grid.add_widget(hang_grid)

    def to_main(self, *args):
        self.sm.current = 'menu'
        self.sm.transition.direction = 'right'

    def post(self, name, data):
        for k, v in data.items():
            if v.text == "":
                popup = Popup(title='Invalid',
                              content=Label(text='Please fill in everything.'),
                              size_hint=(None, None), size=(200, 200))
                popup.open()
                return False

        payload = {name: [data[k].text for k in data.keys()]}

        s = Server()
        r = s.post(payload)

        if r == 200:
            popup = Popup(title='Success',
                          content=Label(text='Data submitted'),
                          size_hint=(None, None), size=(200, 200))
            popup.open()
            return True
        return False
