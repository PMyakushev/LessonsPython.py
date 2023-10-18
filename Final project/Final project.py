import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
# Да, можно преобразовать столбец в one hot вид без использования функции get_dummies. Вот код, который выполняет данную задачу:


import pandas as pd

# Создаем список уникальных значений из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создаем новые столбцы для каждого уникального значения и заполняем их нулями
one_hot_data = pd.DataFrame(0, index=data.index, columns=unique_values)

# Заполняем новые столбцы значениями 1 для соответствующих уникальных значений
one_hot_data.loc[data.index, data['whoAmI']] = 1

# Объединяем исходный DataFrame с новыми столбцами
data_one_hot = pd.concat([data, one_hot_data], axis=1)

data_one_hot.head()