from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt
import sys

class Ui(QtWidgets.QMainWindow):
    currentMission = 0
    currentPage = 0
    DVState = False
    output_te = ""
    def __init__(self):
        super(Ui, self).__init__()       
        uic.loadUi('client.ui', self)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.update)
       
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