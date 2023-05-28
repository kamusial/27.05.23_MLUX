import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

class Touch(Widget):
    btn = ObjectProperty()
    def on_touch_down(self, touch):
        print('Mysz w dole', touch.pos)
        self.btn.opacity = 0.2
        self.btn.size[0] += 10
    def on_touch_move(self, touch):
        print('mysz w ruchu', touch.spos)
        self.btn.pos[1] = touch.pos[1]+20

    def on_touch_up(self, touch):
        print('mysz w gorze', touch.pos[1])
        self.btn.opacity = 1

class My7App(App):
    def build(self):
        return Touch()

if __name__ == '__main__':
    My7App().run()