import tkinter as tk
from models import entry_window, main_window, summary_window
from middlewares import SerialGUI

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Aplicación Espectroscopía")
        self.geometry('740x700')
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        self.serialInterface = SerialGUI()
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
        self.ventana = 0
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (entry_window, main_window, summary_window):
  
            frame = F(container, self)
            
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[self.ventana] = frame
            self.ventana+=1
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.ventana = 0
        self.show_frame(self.ventana)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):

        if cont > 0 :
            self.menu_init()

        frame = self.frames[cont]
        frame.tkraise()

    def SerialGUI(self):
        return self.serialInterface

    def menu_init(self):

        mainmenu = tk.Menu(self, bg="#889E81")
        mainmenu.add_command(label = "Save")  
        mainmenu.add_command(label = "Load")
        mainmenu.add_command(label = "Exit", command= self.destroy)
        
        self.config(menu = mainmenu)