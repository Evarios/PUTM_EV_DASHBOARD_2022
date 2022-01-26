from PyQt5 import QtWidgets, uic, QtCore, QtSerialPort
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt
import sys
from values import *
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


    def update(self):
        self.currentSpeed += 1
        if self.currentSpeed <= 250:
            self.SPEED_speed.setText(str(self.currentSpeed))
        else:
            self.currentSpeed = 0
        
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