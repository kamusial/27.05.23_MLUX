import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text='Imie'))
        self.imie = TextInput(multiline=False)
        self.inside.add_widget(self.imie)

        self.inside.add_widget(Label(text='Nazwisko'))
        self.nazwisko = TextInput(multiline=False)
        self.inside.add_widget(self.nazwisko)

        self.inside.add_widget(Label(text='wiek'))
        self.wiek = TextInput(multiline=False)
        self.inside.add_widget(self.wiek)

        self.add_widget(self.inside)

        self.slij = (Button(text='Slij', font_size=40))
        self.slij.bind(on_press=self.nacisniety_slij)
        self.add_widget(self.slij)

        self.czysc = (Button(text='Czysc', font_size=40))
        self.czysc.bind(on_release=self.nacisniety_czysc)
        self.add_widget(self.czysc)

    def nacisniety_slij(self, instance):
        print('nacisniety')
        imie = self.imie.text
        nazwisko = self.nazwisko.text
        wiek = self.wiek.text
        print(f'Imie: {imie}, nazwisko: {nazwisko}\nwiek: {wiek}')
        print('Imie: ',imie,', nazwisko: ',nazwisko,'\nwiek: ',wiek)
        if int(wiek) >= 18:
            print('jestes pelnoletni')

    def nacisniety_czysc(self, instance):
        self.imie.text = ''
        self.nazwisko.text = ''
        self.wiek.text = ''
        print('dane wyczyszczone')

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()