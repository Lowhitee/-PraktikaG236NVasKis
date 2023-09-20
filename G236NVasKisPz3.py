import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import matplotlib.colors as mcolors

df = pd.read_csv('C:\\titanic.csv')
fig1 = df[df.SexCode == 1][['Survived', 'Age']]
y_pos = np.arange(len(fig1.Survived))
count = 0
for i in range(0, len(fig1.Survived)):
    count += 1
V = 1307


bc = mcolors.BASE_COLORS

objects = ('Выжившие', 'Люди')
y_pos = np.arange(len(objects))
performance = [count, V]
counts = np.random.randint(0, len(performance), len(objects))
colors = [["r", "b", "g", "w", "y", "m"][int(np.random.randint(0, 6, 1))] for _ in counts]
plt.xticks(rotation=45)
plt.bar(y_pos, performance, align='center', alpha=0.5, color=colors)
plt.xticks(y_pos, objects)
plt.ylabel('Количество людей')
plt.title('Титаник')
plt.show()
