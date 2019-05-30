import os


def str_to_bytes(_var: str) -> bytes:
    return _var.encode()


def bytes_to_str(_bytes) -> str:
    return _bytes.decode('cp1251')


hostnames = ['yandex.ru', 'youtube.com']
for hostname in hostnames:
    response = str(os.system("ping -c 1 " + hostname))
    response_byte = str_to_bytes(response)
    response_str_cyr = bytes_to_str(response_byte)
    print(response_str_cyr)
