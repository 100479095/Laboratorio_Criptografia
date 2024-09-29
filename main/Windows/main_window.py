import tkinter as tk

class Log_Window (tk.Tk):
    def __init__(self, Title = str, width = int, height = int):
        super().__init__()
        self.title(Title)
        self.geometry(f"{width}x{height}")
        self.minsize(width, height)

        self.mainloop()