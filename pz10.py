import pandas as pd
import re

df = pd.read_excel("C:\Vassev Kiselev\Машина 1.xlsx")

df['Группа компонента'] = df.apply(lambda row: 'Сборка' if row['Наименование компоненты'] in ["Кузов","Каркас", "Салон", "Подвеска", "Двигатель", "Трансмиссия"] else 'Компонент', axis=1)

krepezh = {'Болт', 'Гайка', 'Штифт', 'Шайба', 'Шуруп'}
decor = {'Коврики', 'Подушки'}


def categorize(row):
    if row['Наименование компоненты'] in krepezh:
        return 'Крепеж'
    elif row['Наименование компоненты'] in decor:
        return 'Декор'
    elif 'Сборка' in row['Группа компонента']:
        return 'Сборка'
    else:
        return 'Детали'


df['Категория'] = df.apply(categorize, axis=1)

df['Код компоненты'].str.findall(r'[A-Za-z]')

def proizvoditel(component):
    if component.isnumeric() or re.match(r'[A-Za-z]', component):
        return 'Иностранное'
    elif 'ГОСТ' in component:
        return 'РФ по ГОСТ'
    elif any(char.isalpha() for char in component):
        return 'РФ'

df['Производитель'] = df['Код компоненты'].apply(proizvoditel)

df.to_excel('C:\Vassev Kiselev\Машина 1-новая.xlsx', index=False)
print(df)