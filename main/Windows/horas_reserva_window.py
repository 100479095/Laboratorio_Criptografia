import tkinter as tk
from tkinter import ttk, messagebox
from Store.Reservation_Store import ReservationStore



class HorasReservaWindow(tk.Tk):
    def __init__(self, user, ID):
        super().__init__()
        self.user = user
        self.ID = ID
        self.title("Time_Slots_Window")
        self.geometry("700x400")
        self.resizable(False, False)
        self.create_horas_reserva_window()

        self.mainloop()
    def create_horas_reserva_window(self):
        main_frame = tk.Frame(self, width=700, height=500, bg="lightblue")
        main_frame.pack()
        main_title = tk.Label(main_frame, text="Escoge una hora", font=("Verdana", 24), bg="darkblue", fg="white")
        main_title.grid(column=0, row=0, columnspan=5, ipadx=225, ipady=30, padx=0, pady=0)

        #Botones
        hora1_button = tk.Button(main_frame, text="12:00", font=("Verdana", 20), bg="darkblue", fg="white",
                                 command=lambda:self.escoger_reserva(12))
        hora1_button.grid(column= 0, row= 3, ipadx=5, ipady=7, padx=50, pady=30)

        hora2_button = tk.Button(main_frame, text="13:00", font=("Verdana", 20), bg="darkblue", fg="white",
                                 command=lambda:self.escoger_reserva(13))
        hora2_button.grid(column=1, row=3, ipadx=5, ipady=7, padx=50, pady=30)

        hora3_button = tk.Button(main_frame, text="14:00", font=("Verdana", 20), bg="darkblue", fg="white",
                                 command=lambda:self.escoger_reserva(14))
        hora3_button.grid(column= 2, row= 3, ipadx=5, ipady=7, padx=50, pady=30)

        hora4_button = tk.Button(main_frame, text="15:00", font=("Verdana", 20), bg="darkblue", fg="white",
                                 command=lambda:self.escoger_reserva(15))
        hora4_button.grid(column= 0, row= 4, ipadx=5, ipady=7, padx=50, pady=20)

        hora5_button = tk.Button(main_frame, text="16:00", font=("Verdana", 20), bg="darkblue", fg="white",
                                 command=lambda:self.escoger_reserva(16))
        hora5_button.grid(column= 1, row= 4, ipadx=5, ipady=7, padx=50, pady=20)

        hora6_button = tk.Button(main_frame, text="17:00", font=("Verdana", 20), bg="darkblue", fg="white",
                                 command=lambda:self.escoger_reserva(17))
        hora6_button.grid(column= 2, row= 4, ipadx=5, ipady=7, padx=50, pady=20)

        Cancelar_button = tk.Button(main_frame, text="Cancelar", font=("Verdana", 16), bg="darkblue", fg="white",
                                    command=lambda:self.cancelar())
        Cancelar_button.grid(column= 2, row= 5, ipadx=0, ipady=4, padx=50, pady=3)
    def escoger_reserva(self, hora):
        from Windows.reservar_window import Reservar_Window
        store = ReservationStore()
        reservado = store.reservar(self.user, self.ID, hora)
        if reservado == False:
            messagebox.showerror("Error de reserva", "Hora no disponible")
        else:
            self.destroy()
            Reservar_Window(self.user)
    def cancelar(self):
        from Windows.reservar_window import Reservar_Window
        self.destroy()
        Reservar_Window(self.user)



