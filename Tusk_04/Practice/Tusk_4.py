# У Вани и Пети есть ошибки в их кодах,
#  и они не совпадают с условием задачи. 
# Их код нужно исправить так:
# У Вани: логика для поиска максимального числа неверна в его коде. 
# Также исходное значение 'max_number' должно быть -1, 
# поскольку в последовательности содержатся неотрицательные числа. 
# Вот как должен выглядеть исправленный код:

# Ваня: Не рабочий
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#   max_number = n
# print(max_number)

# Ваня: рабочий исправлено 2 ошибки
# n = int(input())
# max_number = -1
# while n != 0:
#     if max_number < n:
#         max_number = n
#     n = int(input())
# print(max_number)

# У Пети: условие для цикла while должно проверять ввод на ненулевое значение,
#  и он должен правильно присваивать значение n переменной max_number. 
# Исправленный код должен выглядеть так:

# Петя: Не рабочий
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#   n = max_number
# print(n) 

# Петя: рабочий исправлено 3 ошибки
# n = int(input())
# max_number = -1
# while n != 0:
#     if max_number < n:
#         max_number = n
#     n = int(input())
# print(max_number)


# Задача №29. Решение в группах
# Ваня:
n = int(input())
max_number = 1000
while n != 0:
    n = int(input())
    if max_number > n:       
print(max_number)


# Петя:
n = int(input())
max_number = -1
while n < 0:
    n = int(input())
    if max_number < n:
        n = max_number
print(n)