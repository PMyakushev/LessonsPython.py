# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

def calculate_desks(students):
    total_desks = 0
    if students <= 0:
        return 0
    if students % 2 != 0:
        total_desks += 1
    remaining_desks = calculate_desks(students - 2)
    return total_desks + remaining_desks


classes = input("Введите количество учащихся в каждом классе через пробел: ")
students_list = list(map(int, classes.split()))
desks_needed = calculate_desks(sum(students_list))
print("Необходимое количество парт: ", desks_needed)

# a, b, c = 20, 21, 22
# print(a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2)
