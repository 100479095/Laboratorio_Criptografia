import tkinter as tk

class Reservar_Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Register_Window")
        self.geometry("700x500")
        self.resizable(False, False)
        self.create_reservar_window()

        self.mainloop()
    def create_reservar_window(self):
        main_frame = tk.Frame(self, width=700, height=500, bg="lightblue")
        main_frame.pack()
        main_title = tk.Label(main_frame, text="Menú", font=("Verdana", 24), bg="darkblue", fg="white")
        main_title.grid(column=0, row=0, columnspan=5, ipadx=325, ipady=30, padx=0, pady=0)

        # Títulos
        bienvenida_label = tk.Label(main_frame, text="Bievenido!", font=("Verdana", 32), bg="lightblue", fg="white")
        bienvenida_label.grid(column=2, row=1, ipadx=7, ipady=5, padx=50, pady=0)
