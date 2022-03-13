import socket
import threading

class NetworkHandler:

    def __init__(self):
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 2137
        self.connected = False
    
    def start_connection(self):
        networkHandlerThread = threading.Thread(target=self.init_connection)
        networkHandlerThread.start()

    def init_connection(self):
        print("Waiting for connection")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.TCP_IP, self.TCP_PORT))
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()
        print("Connection established")
        self.connected = True
    
    def send_message(self, message):
        if self.connected == True:
            self.conn.send(message)