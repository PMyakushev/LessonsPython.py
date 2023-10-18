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


# import sys
# def reverse(n):
#     if n == 0:
#         return
#     x = int(sys.stdin.readline()) 
#     reverse(n-1)
#     print(x, end=' ')

# n = int(sys.stdin.readline())
# reverse(n)

seq = input('Введите последовательность чисел, разделенных пробелом: ').split(' ')
seq.reverse()
print(' '.join(seq))
