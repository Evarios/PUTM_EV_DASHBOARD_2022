import can

def startSending():
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=1000000)
    x = 0
    while True:
        msg=can.Message(arbitration_id = 0x01, data=x.to_bytes(8,'big'))
        bus.send(msg)
        x+=1
        if(x== 200):
            x = 0
if __name__ == "__main__":
    startSending()
