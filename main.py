from PyQt5 import QtWidgets, uic, QtCore, QtSerialPort
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt
import sys

from numpy import double
# from values import *
from styles import *
#from messageHandler import handle_messsage

speed = 0
#HV BATT
hv_voltage = 0
hv_charge_percent = 0
hv_avg_temp = 0
hv_max_temp = 0
hv_min_temp = 0
#LV BATT
lv_voltage = 0
lv_charge_percent = 0
lv_avg_temp = 0
lv_max_temp = 0
lv_min_temp = 0
#ENGINE MODE
engine_mode = 1
#MENU ID MATCHING

def handle_messsage(msg):
   #message will be in form: ID:VALUE
   if ":" in msg:
    id_val = msg.split(':')
    update_value(id_val[0], float(id_val[1]))
   
def update_value(id, value):
   #exec("%s = %d" % (id, value))
    if id == "speed":
        global speed
        speed = int(value)
    #hv values
    elif id == "hv_voltage":
        global hv_voltage
        hv_voltage = value
    elif id == "hv_charge_percent":
        global hv_charge_percent
        hv_charge_percent = int(value)
    elif id == "hv_avg_temp":
        global hv_avg_temp
        hv_avg_temp = value
    elif id == "hv_max_temp":
        global hv_max_temp
        hv_max_temp = value              
    elif id == "hv_min_temp":
        global hv_min_temp
        hv_min_temp = value
    #lv values
    elif id == "lv_voltage":
        global lv_voltage
        lv_voltage = value
    elif id == "lv_charge_percent":
        global lv_charge_percent
        lv_charge_percent = int(value)
    elif id == "lv_avg_temp":
        global lv_avg_temp
        lv_avg_temp = value
    elif id == "lv_max_temp":
        global lv_max_temp
        lv_max_temp = value              
    elif id == "lv_min_temp":
        global lv_min_temp
        lv_min_temp = value
    #engine mode
    elif id == "engine_mode":
        global engine_mode
        engine_mode = int(value)    

class Ui(QtWidgets.QMainWindow):
    currentSpeed = 0
    currentPage = 0
    output_te = ""
    def __init__(self):
        super(Ui, self).__init__()       
        uic.loadUi('main.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.update)
        #serial port configuration
        self.serial = QtSerialPort.QSerialPort(
            'COM4',
            baudRate=QtSerialPort.QSerialPort.Baud9600,
            readyRead=self.receive
        )
        self.serial.close()
        self.serial.open(QtCore.QIODevice.ReadWrite)

    @QtCore.pyqtSlot()
    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            print(text)
            handle_messsage(text)


    def update(self):
        #updating speed
        self.SPEED_speed.setText(str(speed))
        self.MENU_speed.setText("SPEED: " + str(speed))
        #updating LV values
        self.MENU_lv.setText("LV " + str(lv_charge_percent) + "%")
        self.LV_charge.setText("Charge level:\n" + str(lv_charge_percent) + "%")
        self.LV_voltage.setText("Voltage:\n" + str(lv_voltage) + "V")
        self.LV_temp.setText("Temerature:\n" + str(lv_avg_temp)+ "°C")
        
        #updating HV values
        self.MENU_hv.setText("HV " + str(hv_charge_percent) + "%")
        self.HV_charge.setText("Charge level:\n" + str(hv_charge_percent) + "%")
        self.HV_voltage.setText("Voltage:\n" + str(hv_voltage) + "V")
        self.HV_temp.setText("Temerature:\n" + str(hv_avg_temp)+ "°C")

        #updating engine mode
        self.MENU_engMode.setText("ENG_MODE\n -> " + str(engine_mode))
        if engine_mode == 1:
            self.ENGMODE_mode.setText("Engine mode: 1 (100% power)")
        elif engine_mode == 2:
            self.ENGMODE_mode.setText("Engine mode: 2 (90% power)")
        
    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(DEACTIVE)
            self.currentPage += 1
            if self.currentPage == 5:
                self.currentPage = 0
            self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(ACTIVE)
            self.stackedWidget.setCurrentIndex(self.currentPage)
        if event.key() == Qt.Key_Up:
            self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(DEACTIVE)
            self.currentPage -= 1
            if self.currentPage == -1:
                self.currentPage = 4
            self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(ACTIVE)
            self.stackedWidget.setCurrentIndex(self.currentPage)
        




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    window.start()
    app.exec_()