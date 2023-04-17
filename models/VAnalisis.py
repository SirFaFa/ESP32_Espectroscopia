
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import matplotlib

#from .VEntrada import entry_window
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

# class summary_window(ttk.Frame):
#     def __init__(self, master, controller):

#         ttk.Frame.__init__(self, master)
#         self.master = master
 
#         frame = ttk.Frame(self)
 
#         style = ttk.Style()
#         style.configure("Custom.TButton",
#                          foreground="black",
#                          background="white",
#                          padding=[10, 10, 10, 10],
#                          font="Verdana 12 underline")
 
#         bttn = ttk.Button(frame, text="Click Me!", style="Custom.TButton")
#         bttn.pack()
 
#         frame.pack(padx = 5, pady = 5)

class summary_window(ttk.Frame):
    def __init__(self, parent, controller):

        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.SerialGUI = self.controller.SerialGUI()
        for r in range(0, 5):
            self.rowconfigure(r, weight=1)
            for c in range(0, 4):
                self.columnconfigure(c, weight=1)

        self.notebook = ttk.Notebook(self)
 
        #Frame 1, 2 and 3
        frame1 = ttk.Frame(self.notebook)
        frame2 = ttk.Frame(self.notebook)
        frame3 = ttk.Frame(self.notebook)

        style = ttk.Style()
        style.configure("Custom.TLabel",
                        foreground="black",
                        background="#889E81",
                        padding=[10, 10, 10, 10],
                        height=10,
                        width=20,
                        font="Verdana 12")
        
        label1 = ttk.Label(frame1, text = "This is Window One", style="Custom.TLabel")
        label1.pack(pady = 50, padx = 20)
        label2 = ttk.Label(frame2, text = "This is Window Two")
        label2.pack(pady = 50, padx = 20)
        label3 = ttk.Label(frame3, text = "This is Window Three")
        label3.pack(pady = 50, padx = 20)
        
        # self.columnconfigure(0, weight=1)

        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)#90A17D

        frame1.pack(fill= tk.BOTH, expand=True)
        frame2.pack(fill= tk.BOTH, expand=True)
        frame3.pack(fill= tk.BOTH, expand=True)
 
        self.notebook.add(frame1, text = "Window 1")
        self.notebook.add(frame2, text = "Window 2")
        self.notebook.add(frame3, text = "Window 3")

        self.notebook.select(frame2)
        print(self.notebook.tab(frame2))
        print(self.notebook.tab(1, "text"))
        
        self.notebook.grid(row=0, column=0, sticky="nsew", padx = 5, pady = 5, rowspan=4, columnspan=5) 
        
        self.label2 = tk.Frame(
            self, bg="#EDF1D6", height=120)
        
        Desired_font = font.Font( family = "Montserrat", 
                                 size = 20, 
                                 weight = "bold")
        
        #self.label2.configure(font=Desired_font)
        
        self.label2.bind('<Button-1>', self.IniciarEsp)
        self.label2.bind('<Enter>', self.Enter_EfectoBoton)
        self.label2.bind('<Leave>', self.Leave_EfectoBoton)

        self.label2.grid(row=5, column=0, sticky="nsew", columnspan=5)    
        self.grid(sticky="nsew")
        

    def IniciarEsp(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.controller.show_frame(1)
        return

    def Enter_EfectoBoton(self, event):
        self.label2.configure(bg="#EDF1D6")

    def Leave_EfectoBoton(self, event):
        self.label2.configure(bg="#3C6255")
        self.dibujar_grafico()

    def dibujar_grafico(self):
        x = np.arange(start=0, stop=1024, step=1)
        y = self.SerialGUI.devuelve_valor()
        if y:
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            a.plot(x, y, 'r')
            a.plot(x, [x//2 for x in y], 'b')

            figure_canvas = FigureCanvasTkAgg(f, self)
            #plt.show()
            figure_canvas.get_tk_widget().grid(row=1, column=1, rowspan=2, columnspan=2)

        print("y no válida")
        # create the toolbar


        



# class summary_window(tk.Frame):

#     def __init__(self, parent, controller):

#         super().__init__(self, parent)

#         main_window.title("Posicionar elementos en Tcl/Tk")
        
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

# import tkinter as tk
# from tkinter import ttk
  
 
# LARGEFONT =("Verdana", 35)
  
# class tkinterApp(tk.Tk):
     
#     # __init__ function for class tkinterApp
#     def __init__(self, *args, **kwargs):
         
#         # __init__ function for class Tk
#         tk.Tk.__init__(self, *args, **kwargs)
         
#         # creating a container
#         container = tk.Frame(self) 
#         container.pack(side = "top", fill = "both", expand = True)
  
#         container.grid_rowconfigure(0, weight = 1)
#         container.grid_columnconfigure(0, weight = 1)
  
#         # initializing frames to an empty array
#         self.frames = {} 
  
#         # iterating through a tuple consisting
#         # of the different page layouts
#         for F in (StartPage, Page1, Page2):
  
#             frame = F(container, self)
  
#             # initializing frame of that object from
#             # startpage, page1, page2 respectively with
#             # for loop
#             self.frames[F] = frame
  
#             frame.grid(row = 0, column = 0, sticky ="nsew")
  
#         self.show_frame(StartPage)
  
#     # to display the current frame passed as
#     # parameter
#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()
  
# # first window frame startpage
  
# class StartPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
         
#         # label of frame Layout 2
#         label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
         
#         # putting the grid in its place by using
#         # grid
#         label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
#         button1 = ttk.Button(self, text ="Page 1",
#         command = lambda : controller.show_frame(Page1))
     
#         # putting the button in its place by
#         # using grid
#         button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
#         ## button to show frame 2 with text layout2
#         button2 = ttk.Button(self, text ="Page 2",
#         command = lambda : controller.show_frame(Page2))
     
#         # putting the button in its place by
#         # using grid
#         button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
          
  
  
# # second window frame page1
# class Page1(tk.Frame):
     
#     def __init__(self, parent, controller):
         
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
#         label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text ="StartPage",
#                             command = lambda : controller.show_frame(StartPage))
     
#         # putting the button in its place
#         # by using grid
#         button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
#         # button to show frame 2 with text
#         # layout2
#         button2 = ttk.Button(self, text ="Page 2",
#                             command = lambda : controller.show_frame(Page2))
     
#         # putting the button in its place by
#         # using grid
#         button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# # third window frame page2
# class Page2(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
#         label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text ="Page 1",
#                             command = lambda : controller.show_frame(Page1))
     
#         # putting the button in its place by
#         # using grid
#         button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
#         # button to show frame 3 with text
#         # layout3
#         button2 = ttk.Button(self, text ="Startpage",
#                             command = lambda : controller.show_frame(StartPage))
     
#         # putting the button in its place by
#         # using grid
#         button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
# # Driver Code
# app = tkinterApp()
# app.mainloop()