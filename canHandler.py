import can
import values
import threading
from networkHandler import *
class CanHandler:

    def __init__(self):
        self.bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=1000000)
        self.logFile = open('log.txt', 'w')
        self.networkHandler = NetworkHandler()
        self.networkHandler.start_connection()
    
    def receive_data(self):
        msg = can.Message()
        byteList = []
        while True:
            msg = self.bus.recv()
            byteList=list(msg.data)
            self.update_value(hex(msg.arbitration_id), byteList[7])
            self.logFile.write(str(msg))
            self.logFile.write('\n')
            self.networkHandler.send_message(str(msg).encode('utf-8'))
    
    def update_value(self, id, value):
        values.canDict[id] = value

    def send_mission(self):
        pass
    
    def start_receiving(self):
        canHandlerThread = threading.Thread(target=self.receive_data)
        canHandlerThread.start()


