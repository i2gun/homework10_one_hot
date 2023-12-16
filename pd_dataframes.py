# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# который состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI':lst})

#----------  Решение ---------------------------

df['whoAmI_human'] = 0
df['whoAmI_robot'] = 0
df.loc[df['whoAmI'] == 'human', 'whoAmI_human'] = 1
df.loc[df['whoAmI'] == 'robot', 'whoAmI_robot'] = 1
df = df.drop(columns='whoAmI')

# вывод аналогичен выводу функции get_dummies():
#      df = pd.get_dummies(df);

df