# Uncomment this to pass the first stage
import socket


def main():

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client, addr = server_socket.accept()
    data = client.recv(1024).decode()
    req = data.split('\r\n')
    path = req[0].split(" ")[1]
    if path == "/":
        response = "HTTP/1.1 200 OK\r\n\r\n".encode()  
    elif path.startswith('/echo'):
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 3\r\n\r\n{path[6:]}".encode()
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
    client.send(response)

if __name__ == "__main__":
    main()
