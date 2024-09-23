"""
Завдання 3

Напишіть функцію-генератор для отримання n перших простих чисел.


"""


from math import sqrt
def simple_check(num:int) -> bool:
    simple = True
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            simple = False
            break
        i += 1
    return simple


def generator_simple(list_of_numbers: list):
    for element in list_of_numbers:
        if simple_check(element):
            yield element


if "__main__" == __name__:
    my_number_list = [i for i in range(1, 21)]
    for number in generator_simple(my_number_list):
        print(number)


