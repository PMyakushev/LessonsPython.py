# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# def fibonachi(n):
#     a, b = 0, 1
#     if n <= b:
#         return print(-1)
#     else:
#         while (a < n):
#             print(a, end=' ')
#             a, b = b, b + a
#         print()
# fibonachi(5)

def fibonacci_position(A):
    fib1, fib2 = 1, 1
    counter = 3
    while fib2 < A:
        fib1, fib2 = fib2, fib1 + fib2
        counter += 1
    if fib2 == A:
        return counter
    return -1
print(fibonacci_position(5))
