from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox


class YourApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        lbl = Label(text='Выберите режим')
        #ch1 = CheckBox(text='asdasdsad')
        b1 = Button(text='button 1')
        b2 = Button(text='button 2')

        layout.add_widget(lbl)
        #layout.add_widget(ch1)
        layout.add_widget(b1)
        layout.add_widget(b2)

        return layout


YourApp().run()