import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5050))

HEADERSIZE = 10

while True:
    fullmessage = ""
    newmessage = True
    while True:
        msg = s.recv(16)
        if newmessage:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            newmessage = False

        fullmessage += msg.decode("utf8")

        if len(fullmessage) - HEADERSIZE == msglen:
            print("full msg received")
            print(fullmessage[HEADERSIZE:])
            newmessage = True
            fullmessage = ""
    print(fullmessage)
