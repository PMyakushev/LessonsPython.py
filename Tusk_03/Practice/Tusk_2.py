# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

arr = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(array)))

new_array = []
for el in arr:
    if el not in new_array:
        new_array.append(el)
print(len(new_array))        


print(len([i for i in enumerate(sorted(arr)) if i[0] == 0 or i[1] != sorted(arr)[i[0] - 1]]))
print(len([i for i in zip(sorted(arr), sorted(arr)[1:] + [sorted(arr)[0]]) if i[0] != i[1]]))
print(len([i for i in range(len(arr)) if min(sorted(arr)[i:]) != min(sorted(arr)[i - 1:])]))
print(len([i for i in range(len(arr)) if arr[i] not in arr[i + 1:]]))
print(len([i for i in range(len(arr)) if arr[i:].count(arr[i]) == 1]))


