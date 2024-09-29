import tkinter as tk

class Log_Window (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Log_Window")
        self.geometry("700x500")
        self.minsize(700, 500)
        self.items_creation()

        self.mainloop()

    def items_creation (self):
        main_title = tk.Label(self, text = "Canchas de Padel", font = ("Verdana", 24), bg="green", fg="white", width="700")
        main_title.pack(anchor = tk.CENTER)
