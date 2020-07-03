import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5050))
s.listen(5)  # Queue of 5.  5 connection maximum
print("Server is Running...")

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    message = "Welcome to the server!!"
    message = f"{len(message):<{HEADERSIZE}}" + message

    clientsocket.send(bytes(message, "utf8"))
    while True:
        time.sleep(3)
        message = f"The time is: {time.time()}"
        message = f"{len(message):<{HEADERSIZE}}" + message
        clientsocket.send(bytes(message, "utf8"))
