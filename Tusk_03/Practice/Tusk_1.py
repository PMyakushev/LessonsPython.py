
# [3, 4, 5, 1, 2]
# for i in range(k):
#     array.append(array[i])
# del array[:k]
# print(array)

# class ArrayAppend():
#     def __init__(self, array, k):
#         self.array = array
#         self.k = k

#     def sortedSet(self):
#         sortedArray = [0] * len(self.array)
#         for i in range(len(self.array)):
#             new_inedex = (i - self.k) % len(self.array)
#             sortedArray[new_inedex] = self.array[i]
#         return sortedArray

# array = [1, 2, 3, 4, 5]
# k = 3

# new_object = ArrayAppend(array, k)
# my_new_array = new_object.sortedSet()
# print(my_new_array)

        
# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# arraySet = set()
# for i in array:
#     arraySet.add(i)
# print(len(arraySet))

# class ArrayUniqua():
#     def __init__(self, array):
#         self.array = array

#     def sortedUniqua(self):
#         arraySet = set()
#         for i in self.array:
#             arraySet.add(i)
#         return arraySet


# array = [1, 1, 2, 0, -1, 3, 4, 4]
# new_object = ArrayUniqua(array)
# my_array_result = new_object.sortedUniqua()
# print(my_array_result)




# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# my_dict =  [{"V": "S001"},
# {"V": "S002"},
# {"VI": "S001"},
# {"VI": "S005"},
# {"VII": " S005 "},
# {" V ":" S009 "},
# {" VIII":" S007 "}]

# unique_values = set()
# for dictionary in my_dict:
#   unique_values.update([value.strip() for value in dictionary.values()])
# print(unique_values)



# class UniqueValuesFinder:
#     def __init__(self, dict_list):
#         self.dict_list = dict_list

#     def find_unique_values(self):
#         unique_values = set()
#         for dictionary in self.dict_list:
#             unique_values.update([value.strip() for value in dictionary.values()])
#         return unique_values

# # Применение
# dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# finder = UniqueValuesFinder(dict_list)
# print(finder.find_unique_values())


# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

array = [0, -1, 5, 2, 3]
count = 0
# for i in range(1, len(array)):
#   if array[i] > array[i-1]:
#     count += 1
# print(count)

class ComparingNumber():
  def __init__(self, array):
    self.array = array

  def my_comparing_mumber(self):
    count = 0
    for i in range(1, len(self.array)):
      if self.array[i] > self.array[]
