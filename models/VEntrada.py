#import VPrincipal


import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk



import os
print(os.path.join(os.path.dirname(__file__), '..', 'static', 'data', 'naranja1.png'))
# results in C:\projects\relative_path\processes\..\data\mydata.json

image_url = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static', 'data', 'naranja1.png'))
# results in C:\projects\relative_path\data\mydata.json
# class main_window(tk.Frame):

#     def __init__(self, parent, controller):

#         super().__init__(self, parent)

#         main_window.title("Ventana Principal")
        
#         main_window.columnconfigure(0, weight=1)

#         main_window.rowconfigure(0, weight=1)
#         main_window.geometry('820x500')
#         self.label1 = tk.Label(
#             self, text="¡Hola, mundo!", bg="#FFA500")
        
#         self.label1.grid(row=0, column=0, sticky="nsew") 

#         self.label2 = tk.Label(
#             self, text="¡Hola, mundo!", bg="#1E90FF")
        
#         self.label2.grid(row=1, column=0, sticky="nsew")    
#         self.grid(sticky="nsew")
#         self.columnconfigure(0, weight=1)

#         self.rowconfigure(0, weight=5)
#         self.rowconfigure(1, weight=1)

LARGEFONT =("Verdana", 35)

class entry_window(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.controller = controller

        #self.title("Posicionar elementos en Tcl/Tk")
        
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        #self.geometry('820x500')
        self.label1 = tk.Label(
            self, bg="black", fg='#40513B')
        
        Desired_font = font.Font( family = "Montserrat", 
                                 size = 30, 
                                 weight = "bold")
        
        self.label1.configure(font=Desired_font)

        # Create a photoimage object of the image in the path
        image_url = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static', 'img', 'naranja1.png'))
        self.img = Image.open(image_url)
        self.img = self.img.resize((200, 190), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)

  
        self.sublabel1 = tk.Label(self, image=self.img, bg="#609966", fg='#40513B')
        #self.sublabel1.image = test

        # # Position image
        self.sublabel1.grid(row=1, column = 0, sticky = "nsew")

        self.sublabel2 = tk.Label(self, text="Bienvenido a la Espectroscopía \n de Impedancia", bg="#609966", fg='#40513B', pady=10)
        self.sublabel2.configure(font=Desired_font)
        # # Position image
        self.sublabel2.grid(row=0, column = 0, sticky = "nsew")

        self.label1.grid(row=0, column=0, sticky="nsew") 

        self.label2 = tk.Label(
            self, text="Iniciar Programa", bg="#EDF1D6", fg='#40513B', width=10, height=3)
        
        Desired_font = font.Font( family = "Montserrat", 
                                 size = 20, 
                                 weight = "bold")
        
        self.label2.configure(font=Desired_font)
        self.label2.configure(bg="#3C6255", fg="#EDF1D6")
        self.label2.bind('<Button-1>', self.IniciarEsp)
        self.label2.bind('<Enter>', self.Enter_EfectoBoton)
        self.label2.bind('<Leave>', self.Leave_EfectoBoton)

        self.label2.grid(row=2, column=0, sticky="nsew")    
        self.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

    def IniciarEsp(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.controller.show_frame(1)
        return

    def Enter_EfectoBoton(self, event):
        self.label2.configure(bg="#EDF1D6", fg="#40513B")

    def Leave_EfectoBoton(self, event):
        self.label2.configure(bg="#3C6255", fg="#EDF1D6")
