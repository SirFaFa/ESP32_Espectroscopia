import tkinter as tk
import tkinter.ttk as ttk

#from models import entry_window
from tkinterApp import tkinterApp

# main_window = tk.Tk()
# app = entry_window(main_window)

def main():

    application = tkinterApp()
    application.mainloop()

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())


#window = tk.Tk()

# window.title('ESPectroscopía de impedancia')

# window.geometry('820x500')
# #window.resizable(False, False)
# frame = tk.Frame(
#     bg='#a75d5d',
#     width=100,
#     height=10,
#     master=window
# )
# btn_1 = tk.Button(
#     frame, 
#     text='Continuar',
#     bg='#7DCE13',
#     fg='#2B7A0B',
#     width=5,
#     height=5
# )

# label_a = tk.Label(
#     text='Espectroscopía de impedancia',
#     fg='#ffc3a1',
#     bg='#a75d5d',
#     width=100,
#     height=20,
#     master=frame
# )


# label_b = tk.Label(
#     text='Espectroscopía de impedancia',
#     fg='#ffc3a1',
#     bg='#a75d5d',
#     width=100,
#     height=10,
#     master=frame
# )


# btn_1.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
# label_a.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
# #label_b.grid(row=2, column=0, sticky="ew", padx=5, pady=5)


# frame.pack()

#window.mainloop()
