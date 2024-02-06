import customtkinter
from djitellopy_reduced import Tello
tello = Tello()
def dron_square():
    global tello
    for i in range(5):
        tello.move_up(50)
        tello.right(50)
        tello.down(50)
        tello.left(50)
def dron_horizont():
    left(50)
    right(50)
    left(50)
    right(50)
    left(50)
    right(50)
    left(50)
    right(50)
    left(50)
    right(50)
def dron_vertical():
    up(50)
    down(100)
    up(100)
    down(100)
    up(100)
    down(100)
    up(100)
    down(100)
    up(100)
    down(100)
    up(50)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.title("eye_trainer")
        self.geometry("400x400")
        self.grid_columnconfigure((0, 1), weight=1)
        self.lbl = customtkinter.CTkLabel(self, text='Выберите режим',height=40, font=("Arial",25,'bold'))
        self.lbl.grid(row=0, column=0, padx=20, pady=40, sticky="ew", columnspan=2)        
        self.vertical_cb = customtkinter.CTkCheckBox(self, text="по вертикали",font=("Arial",20,'bold'))
        self.vertical_cb.grid(row=1, column=0, padx=40, pady=(0, 20), sticky='w')
        self.horizontal_cb = customtkinter.CTkCheckBox(self, text="по горизонтали",font=("Arial",20,'bold'))
        self.horizontal_cb.grid(row=2, column=0, padx=40, pady=(0, 20), sticky='w')
        self.square_cb = customtkinter.CTkCheckBox(self, text="по квадрату",font=("Arial",20,'bold'))
        self.square_cb.grid(row=3, column=0, padx=40, pady=(0, 20), sticky='w')
        self.fly_btn = customtkinter.CTkButton(self, text="Взлёт", command=self.fly,height=40,font=("Arial",20,'bold'))
        self.fly_btn.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.land_btn = customtkinter.CTkButton(self, text="Посадка", command=self.posadka,height=40,font=("Arial",20,'bold'))
        self.land_btn.grid(row=5, column=0, padx=20, pady=0, sticky="ew", columnspan=2)

    def fly(self):
        start()
        takeoff()
        up(100)
        if self.horizontal_cb.get():
            dron_horizont()
        if self.vertical_cb.get():
            dron_vertical()
        if self.square_cb.get():
            dron_square()
        land()
    def posadka(self):
        land()

app = App()
app.mainloop()