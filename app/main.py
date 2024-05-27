# Uncomment this to pass the first stage
import socket


def main():

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client, addr = server_socket.accept()
    data = client.recv(1024).decode()
    req = data.split('\r\n')
    print(req)
    if req[0].split(" ")[1] != "/":
        response = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
    else:
        response = "HTTP/1.1 200 OK\r\n\r\n".encode()
    client.send(response)

if __name__ == "__main__":
    main()
