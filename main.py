from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
import kivy

Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')

class MyRoot(BoxLayout):

    Config.set('graphics', 'resizable', 1)
    # Config.set('graphics', 'width', '400')
    # Config.set('graphics', 'height', '200')

    def __init__(self):
        super(MyRoot, self).__init__()

    def calc_symbol(self, symbol):
        self.calc_field.text += symbol


class AndroidCalculator(App):

    def build(self):
        return MyRoot()


androidcalculator = AndroidCalculator()
androidcalculator.run()
