# class Fibonache():
#     def __init__(self):
#         self.fib = {0: 0, 1: 1}

#     def fibFunc(self, n):
#         if n not in self.fib:
#             self.fib[n] = self.fibFunc(n - 1) + self.fibFunc(n - 2)
#         return self.fib[n]


# fib = Fibonache()
# print(fib.fibFunc(7))

# n = 7
# fib = {0: 0, 1: 1}
# def fibFunc(n):
#         if n not in fib:
#             fib[n] = fibFunc(n - 1) + fibFunc(n - 2)
#         return fib[n]

# print(fibFunc(n))

class Huker():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def marksBook(self, index = 0):
        min_mark = min(self.marks)
        max_mark = max(self.marks)
        if index == len(self.marks):
            return self.marks
        else:
            if __name__ == '__main__':
                if self.marks[index] == max_mark:
                    self.marks[index] = min_mark
                return self.marksBook(index + 1)



vasiliy = Huker("Василий", [1, 3, 3, 3, 4])

print(vasiliy.marksBook())


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


# class ReverseSequence:
#     def __init__(self):
#         self.result = None

#     def reverse(self, N, sequence):
#         if N > 1:
#             self.reverse(N - 1, sequence[1:])
#             if self.result is None:
#                 self.result = str(sequence[0])
#             else:
#                 self.result = self.result + ' ' + str(sequence[0])
#         elif N == 1:
#             if self.result is None:
#                 self.result = str(sequence[0])
#             else:
#                 self.result = self.result + ' ' + str(sequence[0])
#         return self.result


# reverse_seq = ReverseSequence()
# print(reverse_seq.reverse(2, ["3", "4"]))
# # Проверка, является ли число простым
# print(num.is_prime())

