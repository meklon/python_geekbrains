import socket

import init


def get_data_from_client(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        client.send(data.upper())
    return data


def main():
    host, port, buffersize, encoding = init.setup_config()

    try:
        sock = socket.socket()
        sock.bind((host, port))
        sock.listen(5)

        print(f'Server was started with {host}:{port}')

        while True:
            client, address = sock.accept()
            print(f'Client was detected {address}')
            data = get_data_from_client(client)
            print(data.decode(encoding))
            client.send(data)
            client.close()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
