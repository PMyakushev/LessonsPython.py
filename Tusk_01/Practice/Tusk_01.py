# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
from math import ceil

n = int(input("Введите сколько проезжает машина в день: "))
m = int(input("Введите длину маршрута: "))


def drive_car(n, m):
    result = m / n
    return ceil(result)


result = drive_car(n, m)

print(result)
print(ceil(m / n))
print((m + n - 1) // n)