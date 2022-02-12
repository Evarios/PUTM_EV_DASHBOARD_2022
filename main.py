from PyQt5 import QtWidgets, uic, QtCore, QtSerialPort
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt
from messageHandler import handle_messsage
import sys
import values

from styles import *

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
        self.SPEED_speed.setText(str(values.speed))
        self.MENU_speed.setText("SPEED: " + str(values.speed))
        #updating LV values
        self.MENU_lv.setText("LV " + str(values.lv_charge_percent) + "%")
        self.LV_charge.setText("Charge level:\n" + str(values.lv_charge_percent) + "%")
        self.LV_voltage.setText("Voltage:\n" + str(values.lv_voltage) + "V")
        self.LV_temp.setText("Temerature:\n" + str(values.lv_avg_temp)+ "°C")
        
        #updating HV values
        self.MENU_hv.setText("HV " + str(values.hv_charge_percent) + "%")
        self.HV_charge.setText("Charge level:\n" + str(values.hv_charge_percent) + "%")
        self.HV_voltage.setText("Voltage:\n" + str(values.hv_voltage) + "V")
        self.HV_temp.setText("Temerature:\n" + str(values.hv_avg_temp)+ "°C")

        #updating engine mode
        self.MENU_engMode.setText("ENG_MODE\n -> " + str(values.engine_mode))
        if values.engine_mode == 1:
            self.ENGMODE_mode.setText("Engine mode: 1 (100% power)")
        elif values.engine_mode == 2:
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
    values.init()
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    window.start()
    app.exec_()