import socket
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostname()
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

   
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4096)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str(data).encode())
            return self.client.recv(4096)
        except socket.error as e:
            print(e)
