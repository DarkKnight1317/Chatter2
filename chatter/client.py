import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5050))

fullmessage = ""

while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    else:
        fullmessage += msg.decode("utf8")

print(fullmessage)
