import sys
import glob
import serial


class SerialGUI():

    def __init__(self):
        self.data = 0
        self.value = []

    def conectar_esp32(self, port=""):
        try:
            self.esp32 = serial.Serial(port=port, baudrate=115200, timeout=.1)
            return True
        except:
            return False

    def leer_dato(self):
        data = self.esp32.readline().decode('utf-8').replace('\r\n', '')
        return int(data)

    def leer_frecuencia(self, frecuencia):
        self.frecuencia = frecuencia
        comando = "Lectura"
        self.value = []
        self.esp32.write(comando.encode())
        while len(self.value) < 1024 and comando=="Lectura":
            self.value.append(self.leer_dato())

        return self.value 
    
    def devuelve_valor(self):
        if len(self.value) > 0:
            return self.value
        else:
            return False
    
    def cerrarPuerto(self):
        if self.esp32.is_open:
            self.esp32.close()

    def obtener_puertos(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result