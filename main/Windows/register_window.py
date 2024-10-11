import tkinter as tk
from tkinter import ttk

class Register_Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Register_Window")
        self.geometry("700x600")
        self.resizable(False, False)
        self.create_register_window()

        self.mainloop()

    def create_register_window(self):
        main_frame = tk.Frame(self, width=700, height=500, bg="lightblue")
        main_frame.pack()
        main_title = tk.Label(main_frame, text="Registrarse", font=("Verdana", 24), bg="darkblue", fg="white")
        main_title.grid(column=0, row=0, columnspan=5, ipadx=275, ipady=30, padx=0, pady=0)

        # Títulos
        username_label = tk.Label(main_frame, text="Nombre de usuario: ", font=("Verdana"))
        username_label.grid(column=1, row=1, ipadx=7, ipady=5, padx=50, pady=30)
        password_label = tk.Label(main_frame, text="Contraseña: ", font=("Verdana"))
        password_label.grid(column=1, row=2, ipadx=45, ipady=5, padx=50, pady=30)
        fullname_label = tk.Label(main_frame, text="Nombre y Apellido: ", font=("Verdana"))
        fullname_label.grid(column=1, row=3, ipadx=9, ipady=5, padx=50, pady=30)
        creditcard_label = tk.Label(main_frame, text="Tarjeta de Crédito: ", font=("Verdana"))
        creditcard_label.grid(column=1, row=4, ipadx=9, ipady=5, padx=50, pady=30)

        # Entradas
        user_name = tk.StringVar()
        name_entry = tk.Entry(main_frame, textvariable=user_name, font=("Verdana"))
        name_entry.grid(column=3, row=1, ipadx=5, ipady=5, padx=40, pady=20)

        user_pass = tk.StringVar()
        password_entry = tk.Entry(main_frame, textvariable=user_pass, font=("Verdana"), show='*')
        password_entry.grid(column=3, row=2, ipadx=5, ipady=5, padx=40, pady=20)

        user_full_name = tk.StringVar()
        full_name_entry = tk.Entry(main_frame, textvariable=user_full_name, font=("Verdana"))
        full_name_entry.grid(column=3, row=3, ipadx=5, ipady=5, padx=40, pady=20)

        user_creditcard = tk.StringVar()
        creditcard_entry= tk.Entry(main_frame, textvariable=user_creditcard, font=("Verdana"))
        creditcard_entry.grid(column=3, row=4, ipadx=5, ipady=5, padx=40, pady=20)

        register_button = ttk.Button(main_frame, text="Registrate")#, command=self.log_in)  # , font = ("Verdana"))
        register_button.grid(column=2, row=5, ipadx=5, ipady=5, padx=10, pady=10)