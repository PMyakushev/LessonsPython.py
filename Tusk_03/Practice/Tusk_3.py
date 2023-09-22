# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# array = [1, 2, 3, 4, 5]
# k = 3

# for i in range(k):
#     array.append(array[i]) # [1, 2, 3, 4, 5, 1, 2, 3]
# del array[:k]
# print(array)

# new_lst = array[k:] + array[:k]
# print(new_lst)
# k = 3
# lst = [1, 2, 3, 4, 5]

# for i in range(k-1):
#     last_el = lst.pop()
#     lst.insert(0, last_el)
# print(lst)

lst = [1, 2, 3, 4, 5]
k = 3

new_array = [0] * len(lst) # Длина массива 
for el in range(len(lst)):
    new_inedx = (el - k) % len(lst)
    new_array[new_inedx] = lst[el]
print(new_array)
