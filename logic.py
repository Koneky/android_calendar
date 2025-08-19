
import math
import re


class CalculatorLogic:

    def __init__(self):
        self.expression = ""

    def input(self, button_text):
        """Обработка ввода"""
        if button_text.isdigit() or button_text == ".":
            self.expression += button_text
            return self.expression
        
        elif button_text in ["+", "-", "*", "/", "%"]:
            if self.expression and self.expression[-1] not in "+-*/%":
                self.expression += button_text
            return self.expression
        
        elif button_text == "=":
            return self.calculate()
        
        elif button_text == "C":
            self.expression = ""
            return "0"
        
        elif button_text == "CE" or button_text == "<-":
            self.expression = re.sub(r"\d+\.?\d*$", "", self.expression)
            return self.expression if self.expression else "0"
        
        elif button_text == "√":
            return self.sqrt()
        
        elif button_text == "x²":
            return self.square()
        
        elif button_text == "1/x":
            return self.inverse()
        
        elif button_text == "±":
            return self.negate()
        
        return self.expression
    
    def calculate(self):
        try:
            result = str(eval(self.expression.replace("^", "**")))
            self.expression = result
            return self.expression
        except Exception:
            self.expression = ""
            return "Ошибка"
        
    def sqrt(self):
        try:
            value = eval(self.expression)
            result =str(math.sqrt(value))
            self.expression = result
            return self.expression
        except Exception:
            return "Ошибка"
        
    def square(self):
        try:
            value = eval(self.expression)
            result = str(value ** 2)
            self.expression = result
            return self.expression
        except Exception:
            return "Ошибка"
        
    def inverse(self):
        try:
            value = eval(self.expression)
            result = str(1 / value)
            self.expression = result
            return self.expression
        except Exception:
            return "Ошибка"
        
    def negate(self):
        if self.expression:
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression
        return self.expression