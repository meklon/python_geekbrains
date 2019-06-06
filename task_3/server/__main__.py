import json
import socket

import init

MESSAGE: dict = {
    "item": "GFD-14 Neurotoxin",
    "quantity": 23,
    "price": 599.99,
    "buyer": "Andrew Wiggin",
    "date": "2018-08-03T10:51:42"
}


def get_data_from_client(client) -> bytes:
    data = client.recv(1024)

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
            data_by = get_data_from_client(client)
            data = data_by.decode(encoding)
            print(data)
            if 'toxin' in data:
                response = json.dumps(MESSAGE, ensure_ascii=False).encode("utf-8")
            else:
                response = 'No information for you. Try to ask about toxins'
                response = response.encode()

            client.send(response)
            client.close()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
