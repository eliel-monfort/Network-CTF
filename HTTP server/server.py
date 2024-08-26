import socket

IP = '127.0.0.1'
PORT = 46285

def handle_client(client_socket):
    data = client_socket.recv(1024).decode()

    if not data:
        client_socket.send("400 Bad Request Empty Request\r\nContent-Length: 0\r\n\r\n".encode())
        return

    arguments = data.split()
    try:
        if arguments[0] != 'GET':
            client_socket.send("405 Method Not Allowed\r\nContent-Length: 0\r\n\r\n".encode())
            return

    except Exception:
        client_socket.send("400 Bad Request Method Missing\r\nContent-Length: 0\r\n\r\n".encode())
        return

    try:
        version = arguments[2].split('/')
        if version[0] != 'HTTP' or version[1] != '1.0':
            client_socket.send("505 HTTP Version Not Supported\r\nContent-Length: 0\r\n\r\n".encode())
            return

    except Exception:
        client_socket.send("400 Bad Request HTTP Version Missing\r\nContent-Length: 0\r\n\r\n".encode())
        return

    try:
        if arguments[3] != 'Host:':
            client_socket.send("400 Bad Request Host Field Require\r\nContent-Length: 0\r\n\r\n".encode())
            return

    except Exception:
        client_socket.send("400 Bad Request Host Missing\r\nContent-Length: 0\r\n\r\n".encode())
        return

    try:
        if arguments[4] != 'bob.com':
            client_socket.send("400 Bad Request Host Field Invalid\r\nContent-Length: 0\r\n\r\n".encode())
            return

    except Exception:
        client_socket.send("400 Bad Request Host Field Missing\r\nContent-Length: 0\r\n\r\n".encode())
        return

    try:
        if arguments[1] == '/':
            client_socket.send("HTTP/1.0 302 Found\r\nLocation: bob/website/link\r\n\r\n".encode())
            return

        if arguments[1] == 'bob/website/link':
            client_socket.send("HTTP/1.0 200 OK\r\nContent-Length: 0\r\n\r\nhttps://bobbase.vercel.app".encode())
            return

    except Exception:
        client_socket.send("400 Bad Request Requested Item Missing\r\nContent-Length: 0\r\n\r\n".encode())
        return

    client_socket.send("404 Not Found\r\nContent-Length: 0\r\n\r\n".encode())


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    print(f"Server \'bob.com\' listening to connection on localhost")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection success from {client_address}")
        handle_client(client_socket)


if __name__ == '__main__':
    main()
