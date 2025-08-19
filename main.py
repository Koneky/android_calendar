from kivy.core.window import Window
from kivy.utils import platform
from app import CalculatorApp


if __name__ == "__main__":
    if platform in ('win', 'linux', 'macosx'):
        Window.size = (360, 540)
    
    CalculatorApp().run()
