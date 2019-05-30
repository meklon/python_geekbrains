def str_to_bytes(_var: str) -> bytes:
    return _var.encode()


def bytes_to_str(_bytes) -> str:
    return _bytes.decode('utf-8')


def get_byte_content(_bytes: bytes) -> str:
    byte_content = ''
    for _byte in _bytes:
        byte_content = byte_content + str(_byte) + ' '
    return byte_content


def print_data(str_content: str) -> None:
    _bytes = str_to_bytes(str_content)
    byte_content = get_byte_content(_bytes)
    reversed_string_from_bytes = bytes_to_str(_bytes)

    print('String content = {}'.format(str_content))
    print('Byte content = {}'.format(byte_content))
    print('Type after reverse conversion to string = {}'.format(type(reversed_string_from_bytes)))
    print('Content after reverse conversion to string = {}'.format(reversed_string_from_bytes))
    print('')


v1 = 'разработка'
v2 = 'администрирование'
v3 = 'protocol'
v4 = 'standard'

print_data(v1)
print_data(v2)
print_data(v3)
print_data(v4)
