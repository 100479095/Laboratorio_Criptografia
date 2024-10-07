import tkinter as tk

class Register_Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Register_Window")
        self.geometry("700x500")
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
        password_label2 = tk.Label(main_frame, text="Repetir contraseña: ", font=("Verdana"))
        password_label2.grid(column=1, row=3, ipadx=9, ipady=5, padx=50, pady=30)

        # Entradas
        user_name = tk.StringVar()
        name_entry = tk.Entry(main_frame, textvariable=user_name, font=("Verdana"))
        name_entry.grid(column=3, row=1, ipadx=5, ipady=5, padx=40, pady=20)

        user_pass = tk.StringVar()
        password_entry = tk.Entry(main_frame, textvariable=user_pass, font=("Verdana"), show='*')
        password_entry.grid(column=3, row=2, ipadx=5, ipady=5, padx=40, pady=20)

        user_pass2 = tk.StringVar()
        password_entry2 = tk.Entry(main_frame, textvariable=user_pass2, font=("Verdana"), show='*')
        password_entry2.grid(column=3, row=3, ipadx=5, ipady=5, padx=40, pady=20)

