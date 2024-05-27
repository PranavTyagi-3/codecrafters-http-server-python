# Uncomment this to pass the first stage
import socket


def main():

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client, addr = server_socket.accept()
    data = client.recv(1024).decode()
    req = data.split('\r\n')
    if req[0].split(" ")[1] != "/":
        response = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
    else:
        response = "HTTP/1.1 200 OK\r\n\r\n".encode()

    if req[0].split('/')[1] == 'echo':
        response ="HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 3\r\n\r\n"+req[0].split('/')[2].encode()
    client.send(response)

if __name__ == "__main__":
    main()
