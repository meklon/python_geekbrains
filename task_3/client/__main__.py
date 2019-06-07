import json
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
        try:
            data = json.loads(response.decode("utf-8"))
            print('Server responsed with data about item buyer')
            print(f'Item: {data["item"]}, price: {data["price"]}, buyer: {data["buyer"]}')

        except json.decoder.JSONDecodeError:
            print('Cannot decode JSON. Received message: {}'.format(response.decode(encoding)))

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
