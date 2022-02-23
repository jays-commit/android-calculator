from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def calc_symbol(self, symbol):
        self.calc_field.text += symbol


class AndroidCalculator(App):

    def build(self):
        return MyRoot()


androidcalculator = AndroidCalculator()
androidcalculator.run()
