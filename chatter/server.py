import socket
import time
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5050))
s.listen(5)  # Queue of 5.  5 connection maximum
print("Server is Running...")

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    d = {1: "Hey", 2: "There"}
    message = pickle.dumps(d)

    message = bytes(f"{len(message):<{HEADERSIZE}}", "utf8") + message

    clientsocket.send(message)

