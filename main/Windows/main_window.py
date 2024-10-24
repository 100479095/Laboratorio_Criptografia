import tkinter as tk
from tkinter import ttk
from Store.User_Store import UserStore

class Log_Window (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Log_Window")
        self.geometry("700x500")
        self.resizable(False, False)
        self.main_frame()

        self.mainloop()

    def main_frame (self):
        main_frame = tk.Frame(self,width=700, height=500, bg="lightblue")
        main_frame.pack()
        main_title = tk.Label(main_frame, text = "Canchas de Padel", font = ("Verdana", 24), bg="darkblue", fg="white") #width="700")
        main_title.grid(column= 0, row=0, columnspan=5, ipadx= 225, ipady=30, padx=0, pady=0)

        #Títulos
        name_label = tk.Label(main_frame, text="Nombre: ", font = ("Verdana"))
        name_label.grid(column=1, row=1, ipadx=25, ipady=5, padx=50, pady=30)
        password_label = tk.Label(main_frame, text="Contraseña: ", font = ("Verdana"))
        password_label.grid(column=1, row=2, ipadx=5, ipady=5, padx=50, pady=30)

        #Entradas
        user_name = tk.StringVar()
        name_entry = tk.Entry(main_frame, textvariable= user_name, font = ("Verdana"))
        name_entry.grid(column=3, row=1, ipadx=5, ipady=5, padx=40, pady=20)

        user_pass = tk.StringVar()
        password_entry = tk.Entry(main_frame, textvariable= user_pass, font = ("Verdana"), show='*')
        password_entry.grid(column=3, row=2, ipadx=5, ipady=5, padx=40, pady=20)

        #botones
        login_button = ttk.Button(main_frame, text="Log-In", command=lambda:self.log_in(user_name.get(),user_pass.get()))#,
        # font = ("Verdana"))
        login_button.grid(column=3, row=5, ipadx=5, ipady=5, padx=10, pady=10)

        register_button = ttk.Button(main_frame, text="Register", command=self.registrarse)
        register_button.grid(column=1, row=5, ipadx=5, ipady=5, padx=10, pady=10)
    def registrarse(self):
        self.destroy()
        self.import_register()
    def log_in(self, username, password):
        store = UserStore()
        store.autenthicate_user(username, password)
        self.destroy()
        self.import_reservar()

    def import_register(self):
        from .register_window import Register_Window
        Register_Window()
    def import_reservar(self):
        from .reservar_window import Reservar_Window
        Reservar_Window()