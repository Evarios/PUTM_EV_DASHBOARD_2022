from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QFont
import sys

class Ui(QtWidgets.QMainWindow):
    currentSpeed = 0
    def __init__(self):
        super(Ui, self).__init__()       
        uic.loadUi('main.ui', self)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.update)        
    
    def update(self):
        self.currentSpeed += 1
        if self.currentSpeed <= 250:
            self.SPEED.setText(str(self.currentSpeed))
        else:
            self.currentSpeed = 0
        
    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    window.start()
    app.exec_()
    