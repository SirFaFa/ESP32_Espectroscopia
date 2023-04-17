
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import os
import tkinter.ttk as ttk

import sys
 
# setting path
sys.path.append('../middlewares')
 
# importing
from middlewares import SerialGUI

class main_window(ttk.Frame):

    def __init__(self, parent, controller):

        ttk.Frame.__init__(self, parent)

        self.controller = controller
        self.IniciarMainW()

        self.conectado = 0
        self.SerialGUI = self.controller.SerialGUI()
        #self.title("Posicionar elementos en Tcl/Tk")
        
        
        # Create a photoimage object of the image in the path
        # image1 = Image.open("/home/fafa/Desktop/ESP_TFG/static/img/naranjasinfondo-removebg-preview.png")
        # test = ImageTk.PhotoImage(image1)

        # self.sublabel1 = tk.Label(self.label1, image=test)
        # self.sublabel1.image = test

        # # Position image
        # self.sublabel1.place(x=100, y=100)
        # canvas= tk.Canvas(self.label1, width= 600, height= 400)
        

        # # Create a photoimage object of the image in the path
        # image_url = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static', 'img', 'naranja2.png'))
        # img = Image.open(image_url)


        # #Resize the Image using resize method
        # resized_image= img.resize((300,205), Image.ANTIALIAS)
        # new_image= ImageTk.PhotoImage(resized_image)

        # #Add image to the Canvas Items
        # canvas.create_image(10,10, anchor='ns', image=new_image)
        # canvas.grid(row=1, column=0)

        
        #Create a canvas


        self.label2.configure(bg="#3C6255")
        
        self.label2.bind('<Button-1>', self.IniciarEsp)
        self.label2.bind('<Enter>', self.Enter_EfectoBoton)
        self.label2.bind('<Leave>', self.Leave_EfectoBoton)
        self.btnIniciarMedicion.bind('<Button-1>', self.iniciar_espectroscopia)
        self.btnComprobacion.bind('<Button-1>', self.estadoConsola)

           
        self.grid(sticky="nsew")

    def IniciarMainW(self):

        

        #self.geometry('820x500')
        # self.label1 = tk.Label(
        #     self, text="", bg="#609966", fg='#40513B')
        
        # Desired_font = font.Font( family = "Montserrat", 
        #                          size = 30, 
        #                          weight = "bold")
        
        # self.label1.configure(font=Desired_font)

        # self.label1.grid(row=0, column=0, sticky="", columnspan=5) 

        btnImage_url = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static', 'img', 'naranja3.png'))
        self.img = Image.open(btnImage_url)
        	
        self.img = self.img.resize((130, 130), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)

        btnImage_url = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'static', 'img', 'validar.png'))
        self.imgVal = Image.open(btnImage_url)
        	
        self.imgVal = self.imgVal.resize((40, 40), Image.ANTIALIAS)
        self.imgVal = ImageTk.PhotoImage(self.imgVal)

        estiloTexto = ttk.Style()
        estiloTexto.configure("Custom.TLabel",
                        foreground="black",
                        background="#889E81",
                        padding=[10, 10, 10, 10],
                        height=10,
                        width=20,
                        font="Verdana 12")

        estiloTexto2 = ttk.Style()
        estiloTexto2.configure("Custom3.TLabel",
                        foreground="black",
                        background="#3C6255",
                        padding=[10, 10, 10, 10],
                        height=10,
                        width=30,
                        font="Verdana 14")
        
        estiloBtn = ttk.Style()
        estiloBtn.configure("Custom.TButton",
                        foreground="#EDF1D6",
                        background="#D0C9C0",
                        padding=[10, 10, 10, 10],
                        font="Verdana 12 underline")
        #90A17D

        estiloVentana = ttk.Style()
        estiloVentana.configure("Custom.TFrame",
                        foreground="#EDF1D6",
                        background="#889E81",
                        padding=[30, 30, 30, 30],
                        font="Verdana 12 underline")

        estiloSelector = ttk.Style()
        estiloSelector.configure("Custom.TCombobox",
                        foreground="black",
                        background="#889E81",
                        padding=[10, 10, 20, 20],
                        ipadding=[10, 10, 10, 10],
                        font="Verdana 12 underline",
                        width=10,
                        height=8)
        
        

        self.subFrame = tk.Frame(self, width=100, height=100, background="#889E81", relief=tk.GROOVE, bd=3, padx=2, pady=10)

        self.subFrame.rowconfigure(0, weight=1)
        self.subFrame.columnconfigure(0, weight=1)
        self.subFrame.rowconfigure(1, weight=1)
        self.subFrame.columnconfigure(1, weight=1)

        self.subFrame2 = tk.Frame(self, width=300, height=100, background="#889E81", relief=tk.GROOVE, bd=3)

        self.subFrame2.rowconfigure(0, weight=1)
        self.subFrame2.columnconfigure(0, weight=1)
        self.subFrame2.rowconfigure(1, weight=1)
        self.subFrame2.columnconfigure(1, weight=1)

        self.scrolly = tk.Scrollbar(self.subFrame2, bg="#BAC7A7")
        self.scrolly.grid(row=1, column=1, sticky="nsew")

        self.text = tk.Text(self.subFrame2, undo = True, bg="#E5E4CC", fg="#393939", width=50, height=30, yscrollcommand = self.scrolly.set)
        self.scrolly.config(command = self.text.yview)
        self.text.tag_add("TagName", "1.0", "end")
        self.text.grid(row=1, column=0)

        self.labelImagen = tk.Label(self.subFrame2, text="Consola:", foreground="black", background="#889E81")
        self.labelImagen.grid(row=0, column=0, sticky="ew")

        self.subFrame2.grid(row=1, column=1, sticky = "", columnspan=1, rowspan=2)

        self.labelConexion = ttk.Label(self.subFrame, text="Elija el puerto", style="Custom.TLabel")
        self.btnComprobacion = ttk.Button(self.subFrame, image=self.imgVal, style="Custom.TButton")
        self.btnIniciarMedicion = ttk.Button(self, image=self.img, style="Custom.TButton")

        self.puertoSelector = ttk.Combobox(self.subFrame, values=[""], style="Custom.TCombobox")
        self.puertoSelector.grid(row=1, column=1, pady=10)
        self.labelConexion.grid(row=0, column=1, sticky="nsew", pady=5)
        #self.btnComprobacion.configure(state="disabled")

        self.btnComprobacion.grid(row=2, column=1, sticky = "ew", pady=10, padx=10)
        
        self.subFrame.grid(row=1, column=2, sticky = "", columnspan=1, rowspan=1)


        self.btnIniciarMedicion.grid(row=2, column=2, sticky = "", pady=5)

        self.label2 = tk.Frame(
            self, bg="#EDF1D6", height=120)
        
        Desired_font = font.Font( family = "Montserrat", 
                                 size = 20, 
                                 weight = "bold")
        
        #self.label2.configure(font=Desired_font)
        
        # self.label2.rowconfigure(1, weight=1)
        # self.label2.columnconfigure(0, weight=1)
        # self.label2.rowconfigure(2, weight=1)
        # self.label2.columnconfigure(0, weight=1)

        
        # self.progressBar = ttk.Progressbar(self, mode='indeterminate',
        #                                   maximum=200, length=450, orient= tk.HORIZONTAL)
        # self.progressBar.grid(row=5, column=0, sticky="", columnspan=5)
        # self.progressBar.start(interval=2000)
        # self.after(2000)
        self.labelAnalisis = ttk.Label(self, text="Pulsa para ver resultados", style="Custom3.TLabel")

        # self.label21 = self.label2 = tk.Label(
        #     self.label2, text="21", bg="#EDF1D6", fg='#40513B', height=1)
        
        # self.label22 = self.label2 = tk.Label(
        #     self.label2, text="22", bg="#EDF1D6", fg='#40513B', height=1)
        
        # self.label21.grid(row=0, column=0, columnspan=5) 
        # self.label22.grid(row=2, column=0, columnspan=5) 

        self.label2.grid(row=5, column=0, columnspan=5, sticky="nsew") 

        for r in range(0, 5):
            self.rowconfigure(r, weight=1)
            for c in range(0, 4):
                self.columnconfigure(c, weight=1)
                #cell = ttk.Entry(self, width=10)
                #cell.grid(padx=5, pady=5, row=r, column=c, sticky="nsew")
                #cell.insert(0, '({}, {})'.format(r, c))

        self.configure(style="Custom.TFrame")


        

    def IniciarEsp(self, event):
        #print("Mouse position: (%s %s)" % (event.x, event.y))
        if self.SerialGUI.devuelve_valor():
            self.label2.configure(bg="#EDF1D6")
            self.controller.show_frame(2)

    def Enter_EfectoBoton(self, event):
        if self.SerialGUI.devuelve_valor():
            self.label2.configure(bg="#EDF1D6")


    def Leave_EfectoBoton(self, event):
        if self.SerialGUI.devuelve_valor():
            self.label2.configure(bg="#3C6255")
        # self.text.insert("end", "\nThis is some Sample Data \nThis is Line 2 of the Sample Data")
        # self.text.see("end")

    def escribir_consola(self, texto):	
        try:
            self.text.insert("end", str(texto))
            self.text.see("end")
        except:
            print(texto)

    def estadoConsola(self, event):

        ports = self.SerialGUI.obtener_puertos()
        self.puertoSelector.configure(values=ports)

        port = self.puertoSelector.get()
        if self.conectado:
            self.SerialGUI.cerrarPuerto()
        resp = self.SerialGUI.conectar_esp32(port)
        self.escribir_aviso(resp)

        
    def escribir_aviso(self, resp):

        if self.puertoSelector.get() == "":
            self.escribir_consola("\nPorfavor seleccione un puerto")

        # if user select prova show this message 
        else:
            if resp:
                self.escribir_consola("\nConectado a ESP32 ya puede iniciar la espectroscopía de impedancia. \nPulse en la naranja para continuar")
                self.conectado = 1
            else:
                self.escribir_consola("\nPuerto no válido \n Error al conectar ESP32")
                self.conectado = 0

    def iniciar_espectroscopia(self, frecuencia=1000):
        if self.conectado:
            self.escribir_consola("\nIniciando la espectroscopía de impedancia.")
            self.escribir_consola("\nFrecuencia seleccionada: "+ str(frecuencia))
            a = self.SerialGUI.leer_frecuencia(frecuencia=frecuencia)
            for i in a:
                self.escribir_consola("\nValor: "+str(i))

# import tkinter as tk

# def interpolate(color_a, color_b, t):
#     # 'color_a' and 'color_b' are RGB tuples
#     # 't' is a value between 0.0 and 1.0
#     # this is a naive interpolation
#     return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))


# class Application(tk.Tk):

#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.title("Font Color Test")
#         self.geometry("256x64")
#         self.resizable(width=False, height=False)

#         self.label = tk.Label(self, text="Hello World", pady=32)
#         self.label.pack()

#         # On my system (Windows 7, classic theme) this is "SystemButtonFace"
#         label_background_system_color = self.label.cget("background")

#         label_background_16_bit_color = self.label.winfo_rgb(label_background_system_color)

#         # Again, on my system, this is RGB(212, 208, 200)
#         label_background_8_bit_color = tuple(value >> 8 for value in label_background_16_bit_color)

#         # This isn't really required. Making a custom label foreground color just to show it doesn't have to be black.
#         label_foreground_8_bit_color = tuple((255, 0, 0))

#         # I want the the label to "fade in" from the background color to completely red
#         self.start_color = label_background_8_bit_color
#         self.end_color = label_foreground_8_bit_color

#         # Let's say I want a smooth fade in transition at a rate of 60 fps and a duration of 1 second

#         self.duration_ms = 1000
#         self.frames_per_second = 60
#         self.ms_sleep_duration = 1000 // self.frames_per_second
#         self.current_step = 0

#         self.update_label()


#     def update_label(self):

#         t = (1.0 / self.frames_per_second) * self.current_step
#         self.current_step += 1

#         new_color = interpolate(self.start_color, self.end_color, t)
#         self.label.configure(foreground="#%02x%02x%02x" % new_color)

#         if self.current_step <= self.frames_per_second:
#             self.after(self.ms_sleep_duration, self.update_label)


# def main():

#     application = Application()
#     application.mainloop()

#     return 0


# if __name__ == "__main__":
#     import sys
#     sys.exit(main())