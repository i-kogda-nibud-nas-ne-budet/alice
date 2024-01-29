import customtkinter
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x250")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.lbl = customtkinter.CTkLabel(self,text = 'Выберите режим')
        self.lbl.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="s")
        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="n")
        self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 2")
        self.checkbox_2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_3 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 3")
        self.checkbox_3.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

        self.button = customtkinter.CTkButton(self, text="взлет", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.button = customtkinter.CTkButton(self, text="посадка", command=self.button_callback)
        self.button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()