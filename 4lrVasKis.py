import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')
import matplotlib.colors as mcolors
def kubik(n: int) -> list:

    data = []
    while len(data) < n:
        data.append(random.randint(1, 6))
    return data


def count_rate(kub_data: list):
    kub_rate = {}
    for i in kub_data:
        if i in kub_rate:
            continue
        else:
            kub_rate[i] = kub_data.count(i)
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate

def sort_rate(counted_rate: dict):

    sorted_rate = {}
    for key in sorted(counted_rate.keys()):
        sorted_rate[key] = counted_rate[key]
    return sorted_rate

def crate_dataframe(sorted_date: dict):
    df = pd.DataFrame(sorted_date, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))
    return df

def probability_solving(dataframe: pd.DataFrame):
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability
    return dataframe


a1 = kubik(10)
b1 = count_rate(a1)
c1 = sort_rate(b1)
d1 = crate_dataframe(c1)
data = probability_solving(d1)
print(data)
y_pos = len(data)
counts = np.random.randint(0, y_pos, y_pos)
colors = [["r", "b", "g", "w", "y", "m"][int(np.random.randint(0, 6, 1))] for _ in counts]
plt.xlim(0,10)
plt.bar(data['Частота'], data['Вероятность'], align='center', alpha=1, color = colors )
plt.ylabel('Вероятность')
plt.title('Теория вероятности')

plt.show()

