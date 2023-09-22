# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

my_list =  [{"V": "S001"},
{"V": "S002"},
{"VI": "S001"},
{"VI": "S005"},
{"VII": " S005 "},
{" V ":" S009 "},
{" VIII":" S007 "}]

unique_values = set()
for dictionary in my_list:
  unique_values.update([value.strip() for value in dictionary.values()])
print(unique_values)