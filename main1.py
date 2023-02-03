from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
from PyQt5.uic import loadUi
from PyQt5.QtSerialPort import *
from PyQt5.QtCore import QIODevice, QPoint, QTime, QTimer
from PyQt5 import QtCore, QtWidgets
import sys, time
import serial.tools.list_ports


class MyApp(QMainWindow):
    def __init__(self): #se crea el constructor de la clase
        super(MyApp, self).__init__()
        loadUi('d:/Documentos/AppData/C/UNI/Períodos Académicos/Veranos/Verano 05-2022/Programación II/3er Parcial/Examen-Proyecto 3erParcial/interface_1.ui', self) #carga de la GUI mediante loadUi

        ###botones de ventana###
        self.bt_cerrar.clicked.connect(lambda: self.close()) #boton de cerrar
        self.bt_min.clicked.connect(lambda: self.showMinimized()) #boton de minimizar pantalla
        #self.bt_max.clicked.connect(lambda: self.showMaximized()) #boton de maximizar pantalla

        ###eliminar barra de título###
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ###control de botones puerto serial###
        self.serial = QSerialPort()
        self.bt_update.clicked.connect(self.leerPuertos)
        self.bt_connect.clicked.connect(self.conexionSerial)
        self.bt_disconnect.clicked.connect(lambda:self.serial.close())

        ###definir widgets###
        #importacion de los widgets de la GUI:
        #botones, pantallasLCD, leds
        self.serial.readyRead.connect(self.leerData)
        #self.direcc_izq.toggled.connect(self.control_direcc_izq)
        #self.direcc_der.toggled.connect(self.control_direcc_der)
        #self.led_stop.toggled.connect(self.control_led_stop)
        self.slider_gas.valueChanged.connect(self.control_gas_pwm)
        #self.test_door.toggled.connect(self.control_test_door)
        self.lcdTemp = self.findChild(QLCDNumber, "temp_lcd")
        self.lcdRpm = self.findChild(QLCDNumber, "rpm_lcd")
        self.lcdVel = self.findChild(QLCDNumber, "vel_lcd")
        self.lcdKm = self.findChild(QLCDNumber, "km_lcd")

        ###recibir informacion del Arduino###
        #usando libreria: serial
        #self.ard1 = serial.Serial('COM7', 9600) #conexión con el puerto y baudrate
        #time.sleep(1)
        #usando libreria: pyfirmata
        #self.board = Arduino("COM10")
        #self.pin = self.board.get_pin('a:0:i')
        #self.pin1 = self.board.get_pin('d:2:i')
        #self.it = pyfirmata.util.Iterator(self.board)
        #self.it.start()
      
        ###crear timer de lcds###
        #timer: para poder actualizar en tiempo real las pantallas LCD de la GUI
        #self.timer = QTimer()
        #self.timer1 = QTimer()
        #self.timer2 = QTimer()
        #self.timer3 = QTimer()
        #self.timer.timeout.connect(self.control_temp_lcd)
        #self.timer1.timeout.connect(self.control_rpm_lcd)
        #self.timer2.timeout.connect(self.control_vel_lcd)
        #self.timer3.timeout.connect(self.control_km_lcd)

        #iniciar el timer e ir actualizandolo
        #self.timer.start(1000)
        #self.timer1.start(1000)
        #self.timer2.start(1000)
        #self.timer3.start(1000)

        #llamar a la funcion del sensor de temperatura y velocidad, 
        #rpm y contador de KM
        #self.control_temp_lcd() 
        #self.control_rpm_lcd() 
        #self.control_vel_lcd() 
        #self.control_km_lcd() 
        #self.leerData()

        ###mostrar la app###
        self.show()

    ###leer puertos###
    def leerPuertos(self):
        self.baudrates = ['1200', '1400', '4800', '9600', 
                            '19200', '38400', '57600', '115200']
        
        ListaPuertos = []
        puertos = QSerialPortInfo().availablePorts()
        for i in puertos:
            ListaPuertos.append(i.portName())

        self.cb_puertoSerial.clear()
        self.cb_baudrates.clear()
        self.cb_puertoSerial.addItems(ListaPuertos)
        self.cb_baudrates.addItems(self.baudrates)
        self.cb_baudrates.setCurrentText('9600')

    ###conexion al puerto serial###
    def conexionSerial(self):
        self.serial.waitForReadyRead(100)
        self.port = self.cb_puertoSerial.currentText()
        self.baud = self.cb_baudrates.currentText()
        self.serial.setBaudRate(int(self.baud))
        self.serial.setPortName(self.port)
        self.serial.open(QIODevice.ReadWrite)
        

    def leerData(self):
        if not self.serial.canReadLine(): return
        rx = self.serial.readLine()
        x = str(rx, 'utf-8').strip()
        #print(x)

        #Sensor luces
        cad_sensor_luces = x[9:13]
        self.value_luces.setText(str(cad_sensor_luces))
        if cad_sensor_luces == '3.50' or cad_sensor_luces == '3.51' or cad_sensor_luces == '3.52' or cad_sensor_luces == '3.53' or cad_sensor_luces == '3.54' or cad_sensor_luces == '3.55':
            self.test_luces.setChecked(True)
        else:
            self.test_luces.setChecked(False)

        #Sensor de puertas abiertas
        cad_sensor_puertas = x[0]
        if cad_sensor_puertas == '1':
            self.test_door.setChecked(True)
        else:
            self.test_door.setChecked(False)

        #Sensor de rpm
        cad_sensor_rpm =  x[18:25] #x[9:16]
        self.lcdRpm.setDigitCount(10)
        self.lcdRpm.display(cad_sensor_rpm)

        #Sensor de velocidad
        cad_sensor_vel = x[26:36] #x[18:27]
        self.lcdVel.setDigitCount(10)
        self.lcdVel.display(cad_sensor_vel)

        #Contador KM
        cad_sensor_km = x[37:44] #x[22:36] 
        self.lcdKm.setDigitCount(10)
        self.lcdKm.display(cad_sensor_km)

        #Sensor de temperatura
        cad_sensor_temp = x[45:60] #x[37:45]
        self.lcdTemp.setDigitCount(10)
        self.lcdTemp.display(cad_sensor_temp)
     
        #Direccional izquierda
        cad_sensor_izq = x[1]
        if cad_sensor_izq == '1':
            self.direcc_izq.setChecked(True)
        else:
            self.direcc_izq.setChecked(False)

        #Direccional derecha 
        cad_sensor_der = x[2]
        if cad_sensor_der == '1':
            self.direcc_der.setChecked(True)
        else:
            self.direcc_der.setChecked(False)


        #Luz de Stop
        cad_sensor_stop = x[3]
        if cad_sensor_stop == '1':
            self.stop1.setChecked(True)
            self.stop2.setChecked(True)
            #self.stop2.setChecked(True)
        else:
            self.stop1.setChecked(False)
            self.stop2.setChecked(False)
            #self.stop2.setChecked(False)

        #Luz de Stop
        #cad_sensor_stop = x[3]
        #if cad_sensor_stop == '1':
        #    self.direcc_der.setChecked(True)
        #    self.direcc_izq.setChecked(True)
        #else:
        #    self.direcc_der.setChecked(False)
        #    self.direcc_izq.setChecked(False)


    def control_gas_pwm(self, event):
        self.slider_gas.setValue(event)
        sliderGasolina = int(event)
        if sliderGasolina >= 75:
            self.test_gas.setChecked(True)
        else:
            self.test_gas.setChecked(False)

"""
    #funcion de control de pantallaLCD - temperatura
    def control_temp_lcd(self):
        if not self.serial.canReadLine(): return
        ry = self.serial.readLine()
        y = str(ry, 'utf-8').strip()
        cad_sensor_temp = y[10:18]
        self.lcdTemp.setDigitCount(10)
        self.lcdTemp.display(cad_sensor_temp)

    #funcion de control de pantallaLCD - rpm
    def control_rpm_lcd(self):
        pass

    #funcion de control de pantallaLCD - velocidad
    def control_vel_lcd(self):
        pass

    #funcion de control de pantallaLCD - contador KM
    def control_km_lcd(self):
        pass

    def control_luces_pwm(self, event):
        self.slider_luces.setValue(event)
        sliderLuces = '1,' + str(event)
        self.enviarData(sliderLuces)
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp()
    sys.exit(app.exec_())

