import socket, json
from _thread import *
import sys

server = socket.gethostname() 
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

world=[]
s.listen(2)
print("Waiting for a connection, Server Started")
poze=[]
def threaded_client(conn, player):
    global world
    conn.send(json.dumps({"id":player,"world":world}).encode())
    while True:
        try:
            data = conn.recv(4096)
            data = json.loads(data.decode())
            world=data.get("world")
            data=data.get("poz")
            poze[player][0]=data[0]
            poze[player][1]=data[1]
            poze[player][2]=data[2]
            poze[player][3]=data[3]
            

                              
            

            if not data:
                print("Disconnected")
                break
            print(data)
            conn.sendall(json.dumps({"poz":poze,"world":world}).encode())
        except socket.error as e:
            print(e)

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    poze.append([0,0,"",currentPlayer])
    currentPlayer += 1