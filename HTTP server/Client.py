import socket

IP = '127.0.0.1'
PORT = 46285

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    request = (
        "GET bob/website/link HTTP/1.0\r\n"
        "Host: bob.com\r\n"
        "\r\n"
    )
    client_socket.send(request.encode())

    response = client_socket.recv(1024).decode()
    print("Server response:")
    print(response)

    client_socket.close()


if __name__ == '__main__':
    main()
