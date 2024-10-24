import tkinter as tk
from tkinter import ttk

class Reservar_Window(tk.Tk):
    def __init__(self, user):
        super().__init__()
        self.title("Register_Window")
        self.geometry("700x400")
        self.resizable(False, False)
        self.user = user
        self.create_reservar_window()

        self.mainloop()
    def create_reservar_window(self):
        main_frame = tk.Frame(self, width=700, height=500, bg="lightblue")
        main_frame.pack()
        main_title = tk.Label(main_frame, text="Menú", font=("Verdana", 24), bg="darkblue", fg="white")
        main_title.grid(column=0, row=0, columnspan=5, ipadx=325, ipady=30, padx=0, pady=0)

        # Títulos
        name_user = self.user.name.decode("utf-8")
        bienvenida_label = tk.Label(main_frame, text=f"Bievenido {name_user}!", font=("Verdana", 32), bg="lightblue", fg="black")
        bienvenida_label.grid(column=0, row=1, columnspan=5,  ipadx=7, ipady=5, padx=50, pady=0)

        bienvenida_label = tk.Label(main_frame, text=f"Elige la cancha que quieras reservar", font=("Verdana", 24), bg="lightblue",fg="black")
        bienvenida_label.grid(column=0, row=2, columnspan=5,  ipadx=7, ipady=5, padx=50, pady=0)

        cancha_1 = tk.Button(main_frame, text="Cancha 1", font=("Verdana", 20), bg="darkblue", fg="white")
        cancha_1.grid(column=1, row=3, ipadx=5, ipady=7, padx=10, pady=10)

        cancha_2 = tk.Button(main_frame, text="Cancha 2", font=("Verdana", 20), bg="darkblue", fg="white")
        cancha_2.grid(column=2, row=3, ipadx=5, ipady=7, padx=10, pady=10)

        cancha_3 = tk.Button(main_frame, text="Cancha 3", font=("Verdana", 20), bg="darkblue", fg="white")
        cancha_3.grid(column=1, row=4, ipadx=5, ipady=5, padx=10, pady=10)

        cancha_4 = tk.Button(main_frame, text="Cancha 4", font=("Verdana", 20), bg="darkblue", fg="white")
        cancha_4.grid(column=2, row=4, ipadx=5, ipady=5, padx=10, pady=10)
