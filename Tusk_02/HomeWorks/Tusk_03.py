# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

class PowerOfTwoGenerator:
    def __init__(self, N):
        self.N = N

    def generate(self):
        result = []
        i = 0
        while 2 ** i <= self.N:
            result.append(2 ** i)
            i += 1
        return result

generator = PowerOfTwoGenerator(100)
print(generator.generate())