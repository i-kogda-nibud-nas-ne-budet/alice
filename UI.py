import customtkinter

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
        self.fly_btn = customtkinter.CTkButton(self, text="взлет", command=self.button_callback,height=40,font=("Arial",20,'bold'))
        self.fly_btn.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.land_btn = customtkinter.CTkButton(self, text="посадка", command=self.button_callback,height=40,font=("Arial",20,'bold'))
        self.land_btn.grid(row=5, column=0, padx=20, pady=0, sticky="ew", columnspan=2)

    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()