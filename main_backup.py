from PyQt5 import QtWidgets, uic, QtCore, QtSerialPort
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt
import sys
# from values import *
# from styles import *
from messageHandler import handle_messsage

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
#MENU ID MATCHING

def handle_messsage(msg):
   #message will be in form: ID:VALUE
   id_val = msg.split(':')
   update_value(id_val[0], int(id_val[1]))
   
def update_value(id, value):
   #exec("%s = %d" % (id, value))
   if(id == "speed"):
        global speed
        speed = value

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