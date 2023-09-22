# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

input_string = "a a a b c a a d c d d"
result = []
counts = {}

# Разделить строку на отдельные символы
characters = input_string.split()

for char in characters:
  if char in counts:
    counts[char] += 1
    result.append(f"{char}_{counts[char]}")
  else:
    result.append(char)
    counts[char] = 1   
print(' '.join(result))


# lst = "a a a b c a a d c d d"
# res = {}
# for el in lst:
#   if el in res:
#     print(f"{el}_{res[el]}", end = '')
#   else:
#     print(el, end = '')
#   res[el] = res.get(el, 0) + 1
  










# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


# array_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"


# new_array_set = set ()
# for el in array_str.split():
#   new_array_set.add(el)
# print(len(new_array_set))
# print(new_array_set)


# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах





# У Вани и Пети есть ошибки в их кодах,
#  и они не совпадают с условием задачи. 
# Их код нужно исправить так:
# У Вани: логика для поиска максимального числа неверна в его коде. 
# Также исходное значение 'max_number' должно быть -1, 
# поскольку в последовательности содержатся неотрицательные числа. 
# Вот как должен выглядеть исправленный код:

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

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

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 

# n = int(input())
# max_number = -1
# while n != 0:
#     if max_number < n:
#         max_number = n
#     n = int(input())
# print(max_number)

# Теперь оба исправленные варианта кода правильно определяют и 
# выводят наибольшее число в последовательности, заканчивающейся нулем.



# Вот несколько хороших книг для изучения Python:

# "Автоматизация скучных задач с Python" Эла Свейгарта. Отличная книга для начинающих - с примерами и упражнениями.

# "Python. Подробный справочник" Дэвид Бизли. Полезная книга, охватывающая все аспекты языка.

# "Python. Основы программирования" Эрик Мэтиз. Хорошее введение в программирование с нуля.

# "Python для сложных задач" Дэн Бейдер. Разбирает сложные концепции и библиотеки.

# "Python. К вершинам мастерства" Лучано Рамальо. Продвинутый уровень, много примеров.

# "Python. Погружение в Python 3" Марк Лутц. Подробнейшее руководство по языку от авторитетного эксперта.

# "Совершенный код" Дастин Босвелл. Лучшие практики написания чистого, понятного кода.

# "Python для детей" Джейсон Бриггс. Отличная книга для детей и подростков, желающих научиться программировать.

# В целом начинать лучше с книг для новичков, а затем переходить к более продвинутым. Также полезно читать официальную документацию по языку.