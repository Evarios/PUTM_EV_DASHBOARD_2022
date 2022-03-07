import can
import values
def startReceiving():
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=1000000)
    msg = can.Message()
    byteList = []
    while True:
        msg = bus.recv()
        byteList=list(msg.data)
        update_value(hex(msg.arbitration_id), byteList[7])

def update_value(id, value):
    values.canDict[id] = value

def send_mission():
    pass