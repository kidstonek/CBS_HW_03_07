"""
Завдання 2

Виведіть із списку чисел список квадратів парних чисел.
Використовуйте 2 варіанти рішення: генератор та цикл
"""



def generator_sqr(obj: list):
   for number in obj:
      if number % 2 == 0:
         yield number ** 2





if "__main__" == __name__:
   my_list = [25, 2, 8, 4, 4, 5, 10]
   print(my_list)
   print('=============')
   print('генератор')

   for i in generator_sqr(my_list):
      print(i, end=' ')
   print()
   print('=============')
   #  цикл
   print('цикл')
   for i in my_list:
      if i % 2 == 0:
         print(i ** 2, end=' ')