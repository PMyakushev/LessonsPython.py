# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

n = int(input(("Введите число n: ")))
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)

class Factorial:
    def __init__(self, n):
        self.n = n

    def calculate_factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.calculate_factorial(n-1)

    def result(self):
        if self.n < 0:
            return "Извините, факториал не существует для отрицательных чисел"
        else:
            return self.calculate_factorial(self.n)

factorial_instance = Factorial(n)
print(factorial_instance.result())