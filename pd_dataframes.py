# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# который состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI':lst})
