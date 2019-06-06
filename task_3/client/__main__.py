import socket

import init


def main():
    host, port, buffersize, encoding = init.setup_config()

    try:
        sock = socket.socket()
        sock.connect((host, port))
        print('Client started')
        data = input('Enter data: ')
        sock.send(data.encode(encoding))

        response = sock.recv(buffersize)
        print(response.decode(encoding))

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
