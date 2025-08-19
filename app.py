from kivymd.app import MDApp
from ui import CalculatorUI


class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark" # Dark/Light
        return CalculatorUI()
