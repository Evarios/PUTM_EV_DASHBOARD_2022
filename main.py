from PyQt5 import QtWidgets, uic, QtCore#, QtSerialPort
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt
from canHandler import *
import sys
import values
import threading

from styles import *

class Ui(QtWidgets.QMainWindow):
    currentMission = 0
    currentPage = 0
    DVState = False
    output_te = ""
    def __init__(self):
        super(Ui, self).__init__()       
        uic.loadUi('main.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.update)

    def update(self):
        #updating speed
        #self.SPEED_speed.setText(str(values.canDict["0x1"]))
        self.MENU_speed.setText("SPEED: " + str(values.valuesDict["speed"]))
        self.SPEED_bar.setValue(values.canDict["0x1"])
        #updating LV values
        self.MENU_lv.setText("LV " + str(values.valuesDict["lv_charge_percent"]) + "%")
        self.LV_charge.setText("Charge level:\n" + str(values.valuesDict["lv_charge_percent"]) + "%")
        self.LV_voltage.setText("Voltage:\n" + str(values.valuesDict["lv_voltage"]) + "V")
        self.LV_temp.setText("Temerature:\n" + str(values.valuesDict["lv_avg_temp"])+ "°C")
        
        #updating HV values
        self.MENU_hv.setText("HV " + str(values.valuesDict["hv_charge_percent"]) + "%")
        self.HV_charge.setText("Charge level:\n" + str(values.valuesDict["hv_charge_percent"]) + "%")
        self.HV_voltage.setText("Voltage:\n" + str(values.valuesDict["hv_voltage"]) + "V")
        self.HV_temp.setText("Temerature:\n" + str(values.valuesDict["hv_avg_temp"])+ "°C")

        #updating engine mode
        self.MENU_engMode.setText("ENG_MODE\n -> " + str(values.valuesDict["engine_mode"]))
        if values.valuesDict["engine_mode"] == 1:
            self.ENGMODE_mode.setText("Engine mode: 1 (100% power)")
            
        elif values.valuesDict["engine_mode"] == 2:
            self.ENGMODE_mode.setText("Engine mode: 2 (90% power)")
        #print(values.canDict)
        
    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            if self.DVState == False:
                self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(DEACTIVE)
                self.currentPage += 1
                if self.currentPage == 5:
                    self.currentPage = 0
                self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(ACTIVE)
                self.stackedWidget.setCurrentIndex(self.currentPage)
            else:
                send_mission()
        elif event.key() == Qt.Key_Up:
            if self.DVState == False:
                self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(DEACTIVE)
                self.currentPage -= 1
                if self.currentPage == -1:
                    self.currentPage = 4
                self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(ACTIVE)
            self.stackedWidget.setCurrentIndex(self.currentPage)
        elif event.key() == Qt.Key_D:
            if self.currentPage != 5:
                self.DVState = True
                self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(DEACTIVE)
                self.currentPage = 5
                self.stackedWidget.setCurrentIndex(self.currentPage)
                self.currentMission = 0
                self.DV_current_mission.setText(values.DV_MISSIONS[self.currentMission])
            else:
                self.DVState = False
                self.currentPage = 1
                self.stackedWidget.setCurrentIndex(self.currentPage)
                self.menuBar.itemAt(self.currentPage).widget().setStyleSheet(ACTIVE)
        elif event.key() == Qt.Key_Right and self.DVState == True:
            self.currentMission += 1
            if self.currentMission == len(values.DV_MISSIONS):
                self.currentMission = 0
            self.DV_current_mission.setText(values.DV_MISSIONS[self.currentMission])
        elif event.key() == Qt.Key_Left and self.DVState == True:
            self.currentMission -= 1
            if self.currentMission == -1:
                self.currentMission = len(values.DV_MISSIONS)-1
            self.DV_current_mission.setText(values.DV_MISSIONS[self.currentMission])    
            

if __name__ == "__main__":
    canHandlerThread = threading.Thread(target=startReceiving)
    canHandlerThread.start()
    values.init()
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    window.start()
    app.exec_()