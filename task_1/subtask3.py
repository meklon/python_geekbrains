def str_to_bytes(_var) -> bytes:
    return bytes(_var, 'utf-8')


def get_byte_content(_bytes: bytes) -> str:
    byte_content = ''
    for _byte in _bytes:
        byte_content = byte_content + str(_byte) + ' '
    return byte_content


def get_len_bytes(_bytes: bytes) -> int:
    return len(_bytes)


def print_data(str_content: str) -> None:
    _bytes = str_to_bytes(str_content)
    byte_content = get_byte_content(_bytes)
    len_bytes = get_len_bytes(_bytes)

    print('String content = {}'.format(str_content))
    print('Type after byte conversion = {}'.format(type(_bytes)))
    print('Byte content = {}'.format(byte_content))
    print('Variable length in byte format = {}'.format(len_bytes))
    print('')


var_1: str = 'attribute'
var_2: str = 'класс'
var_3: str = 'функция'
var_4: str = 'type'

print_data(var_1)
print_data(var_2)
print_data(var_3)
print_data(var_4)

# А что не так-то? Имелось в виду, что type - зарезервированное имя? Все нормально конвертируется.
