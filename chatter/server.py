import socket
import select

HEADER = 10
IP = "127.0.0.1"
PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               # Defining server socket with IP address and the stream
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))                                                  # Binding server socket with the IP and the PORT
server_socket.listen()                                                          # Starting Server to wait or listen for conenctions from clients

print("SERVER IS UP...")

sockets_list = [server_socket]                                                 # List containing all the sockets
clients = {}                                                                   # dictionary containing al the clients


def receive_message(client_socket):                                            # Receiving message funtion
    try:
        message_header = client_socket.recv(HEADER)                             # defining message header

        if not len(message_header):        # If the message is not null
            return False
        message_length = int(message_header.decode("utf8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user
            username = user['data'].decode('utf8')
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username: {username}")

        else:
            message = receive_message(notified_socket)

            if message is False:
                clientname = clients[notified_socket]["data"].decode("utf8")
                print(f"Closed connection from {clientname}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            username = user['data'].decode("utf8")
            msg = user['data'].decode('utf8')
            print(f"Received message from {username}: message: {msg}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]
