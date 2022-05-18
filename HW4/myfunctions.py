"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    return '*' * 10


print('simple_separator(): ', simple_separator())
print(simple_separator() == '**********')  # True
print()


def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    return '*' * count


print('long_separator(3):', long_separator(3))
print(long_separator(3) == '***')  # True
print('long_separator(4):', long_separator(4))
print(long_separator(4) == '****')  # True
print()


def separator(symbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param symbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    return symbol * count


print('separator(\'-\', 10):', separator('-', 10))
print(separator('-', 10) == '----------')  # True
print('separator(\'#\', 5):', separator('#', 5))
print(separator('#', 5) == '#####')  # True
print()


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********
    Hello World!
    ##########
    :return: None
    """
    print('**********\nHello World!\n##########')


'''
**********
Hello World!
##########
'''
hello_world()
print()


def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********
    Hello {who}!
    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print('**********\nHello', who, '\n##########')


'''
**********
Hello World!
##########
'''
hello_who()
print()

'''
**********
Hello Max!
##########
'''
hello_who('Max')
print()

'''
**********
Hello Kate!
##########
'''
hello_who('Kate')
print()


def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    args_sum = 0
    for n in args:
        args_sum += n
    # функция создана только для целых показателей степени
    power = int(power)
    mult = 1
    if power > 0:
        for i in range(power):
            mult *= args_sum
        return mult
    elif power < 0:
        for i in range(power * (-1)):
            mult /= args_sum
        return mult
    else:
        # нулевая степень, power == 0
        if args_sum != 0:
            return mult
        else:
            return None


print('pow_many(1, 1, 2) =', pow_many(1, 1, 2))
print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3

print('pow_many(1, 2, 3) == 5) =', pow_many(1, 2, 3))
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5

print('pow_many(2, 1, 1) =', pow_many(2, 1, 1))
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4

print('pow_many(3, 2) == 8) =', pow_many(3, 2))
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8

print('pow_many(2, 1, 2, 3, 4) =', pow_many(2, 1, 2, 3, 4))
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100
# Отрицательная степень
print('pow_many(-2, 1, 2, 3, 4) =', pow_many(-2, 1, 2, 3, 4))
print(pow_many(-2, 1, 2, 3, 4) == 0.01)  # True -> (1 + 2 + 3 + 4)**(-2) == 10**(-2) == 1/100
# Нулевая степень
print('pow_many(0, 1, 2, 3, 4) =', pow_many(0, 1, 2, 3, 4))
print(pow_many(0, 1, 2, 3, 4) == 1)  # True -> (1 + 2 + 3 + 4)**(0) == 10**0 == 0
# ноль в нулевой степени
print('pow_many(0, 1, 2, -1, -2) =', pow_many(0, 1, 2, -1, -2))


def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for k, v in kwargs.items():
        print(k, '-->', v)


print()
"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)

print()
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    new_iterable = list(filter(function, iterable))
    return new_iterable

print()
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
