'''''
1.Функция с параметрами по умолчанию:
Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
Функция должна выводить эти параметры.
Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
'''''
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(2)
print_params(0,[4,6,4,6])
print_params('dfhf',False,{'5':5})
# print_params("'fg'",'5','fhf',3) # Error
print_params(b = 25), print_params(c = [1,2,3])

'''''
2.Распаковка параметров:
Создайте список values_list с тремя элементами разных типов.
Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
'''''
values_list = [1,'dfdfbds',False]
values_dict = {'a': 546765, 'b': 456, 'c': 21}
print_params(*values_list)
print_params(**values_dict)


'''''
3.Распаковка + отдельные параметры:
Создайте список values_list_2 с двумя элементами разных типов
Проверьте, работает ли print_params(*values_list_2, 42)
'''''
values_list_2 = [1,'ddfgdf']
print_params(*values_list_2, 42)
