import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5050))
s.listen(5)   # Queue of 5.  5 connection maximum

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    message = "Welcome to the server!!"
    message = f"{len(message):<10}" + message

    clientsocket.send(bytes("Welcome to the server", "utf8"))
    clientsocket.close()
