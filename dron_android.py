from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'width', '540')
Config.set('graphics', 'height', '1140')
Config.write()
from djitellopy_reduced import Tello

import logging
logging.disable(logging.CRITICAL)
tello = Tello()

def dron_square():
    global tello
    for i in range(5):
        tello.move_up(50)
        tello.right(50)
        tello.down(50)
        tello.left(50)
def dron_horizont():
    global tello
    for i in range(5):
        tello.move_left(50)
        tello.move_right(50)
def dron_vertical():
    global tello
    for i in range(5):
        tello.move_up(50)
        tello.move_down(100)

class MyInterface(BoxLayout):
    def __init__(self, **kwargs):
        global vertical_cb
        global horizontal_cb
        global square_cb
        global tello

        super(MyInterface, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='Выберите режим', font_size='40sp')
        self.lh1 = BoxLayout(orientation='horizontal')
        self.lh1.size_hint_x = 0.5
        self.lh1.pos_hint = {'x': 0.2}
        self.vertical_cb = CheckBox(color=[255,255,255,255])
        self.vertical_lbl = Label(text='по вертикали', font_size='30sp')
        self.lh1.add_widget(self.vertical_cb)
        self.lh1.add_widget(self.vertical_lbl)
        self.lh2 = BoxLayout(orientation='horizontal')
        self.lh2.size_hint_x = 0.5
        self.lh2.pos_hint = {'x': 0.2}
        self.horizontal_cb = CheckBox(color=[255,255,255,255])
        self.horizontal_lbl = Label(text='по горизонтали', font_size='30sp')
        self.lh2.add_widget(self.horizontal_cb)
        self.lh2.add_widget(self.horizontal_lbl)
        self.lh3 = BoxLayout(orientation='horizontal')
        self.lh3.size_hint_x = 0.5
        self.lh3.pos_hint = {'x': 0.2}
        self.square_cb = CheckBox(color=[255,255,255,255])
        self.square_lbl = Label(text='по квадрату', font_size='30sp')
        self.lh3.add_widget(self.square_cb)
        self.lh3.add_widget(self.square_lbl)
        
        self.fly_btn = Button(text='Взлёт', font_size='40sp', background_color = [1,1,4,1])
        self.fly_btn.bind(on_press = self.fly)
        self.land_btn = Button(text='Посадка', font_size='40sp', background_color = [1,4,1,1])
        self.land_btn.bind(on_press = self.posadka)

        self.add_widget(self.label)
        self.add_widget(self.lh1)
        self.add_widget(self.lh2)
        self.add_widget(self.lh3)
        self.add_widget(self.fly_btn)
        self.add_widget(self.land_btn)
    def fly(self,instance):
        global tello
        tello.connect()
        tello.takeoff()
        tello.move_up(100)
        if self.vertical_cb.active:
            dron_vertical()
        if self.horizontal_cb.active:
            dron_horizont()
        if self.square_cb.active:
            dron_square()
        tello.land()
    def posadka(self,instance):
        global tello
        tello.land()
        


    
class MyApp(App):
    def build(self):
        return MyInterface()
    


if __name__ == '__main__':
    MyApp().run()