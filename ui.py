from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from logic import CalculatorLogic


class CalculatorUI(BoxLayout):
    expression = StringProperty("")
    result = StringProperty("0")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logic = CalculatorLogic()

    def button_press(self, text):
        output = self.logic.input(text)
        if text == "C":
            self.expression = ""
            self.result = "0"
        elif text == "=":
            self.result = output
        else:
            self.expression = self.logic.expression
