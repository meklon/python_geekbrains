def print_var_type(var1: str, var2: str, var3: str) -> None:
    print('Типы переменных. {}:{}, {}:{}, {}:{}'.format(var1, type(var1), var2, type(var2), var3, type(var3)))


str_dev = 'разработка'
str_socket = 'сокет'
str_decorator = 'декоратор'

print_var_type(str_dev, str_socket, str_decorator)

str_dev = '&#1088;&#1072;&#1079;&#1088;&#1072;&#1073;&#1086;&#1090;&#1082;&#1072;'
str_socket = '&#1089;&#1086;&#1082;&#1077;&#1090;'
str_decorator = '&#1076;&#1077;&#1082;&#1086;&#1088;&#1072;&#1090;&#1086;&#1088;'

print_var_type(str_dev, str_socket, str_decorator)
