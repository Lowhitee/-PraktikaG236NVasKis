import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# plt.style.use('grayscale')
# plt.style.use('seaborn-dark')
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
# plt.style.use('dark_background')
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

def get_plots(arr):
    index = 0
    fig, ax = plt.subplots(2, 2, figsize=[12, 8])
    position = [[0, 0], [1, 0], [0, 1], [1, 1]]
    for i in arr:
        a1 = kubik(i)
        b1 = count_rate(a1)
        c1 = sort_rate(b1)
        d1 = crate_dataframe(c1)
        data = probability_solving(d1)
        y_pos = len(data)
        counts = np.random.randint(0, y_pos, y_pos)
        colors = [["r", "b", "g", "w", "y", "m"][int(np.random.randint(0, 6, 1))] for _ in counts]
        ax[position[index][0], position[index][1]].bar(data['Количество выпаданий'], data['Вероятность'], color = colors)
        ax[position[index][0], position[index][1]].title.set_text(f"Вероятность при {i}")
        index += 1

graf = [10, 100, 1000, 10000]
get_plots(graf)

plt.show()


