import can

def startReceiving():
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=1000000)
    msg = can.Message()
    while True:
        msg = bus.recv()
        print("ID: " + str(msg.arbitration_id) + str(msg.data))

if __name__ == "__main__":
    startReceiving()