class Number:
    def __init__(self, num):
        self.num = num

    def is_prime(self, divisor=None):
        if divisor is None:
            divisor = self.num - 1
        while divisor >= 2:
            if self.num % divisor == 0:
                return False
            else:
                return self.is_prime(divisor - 1)
        return True if self.num != 1 else False


# Создание объекта класса Number
num = Number(5)