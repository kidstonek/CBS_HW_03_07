"""Завдання 1

Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed)."""


def reversed_gen(obj: list):
    for number in range(len(obj)-1,-1, -1):
        yield obj[number]


if "__main__" == __name__:
    my_list = ['first', 2, 8, 4, 4, 5, 'last']
    for i in reversed_gen(my_list):
        print(i)
