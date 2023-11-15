import pandas as pd

df_1 = pd.read_excel("C:\Vassev Kiselev\Машина 1.xlsx")
df_2 = pd.read_excel("C:\Vassev Kiselev\Машина 2.xlsx")

if list(df_1.columns) != list(df_2.columns):
    print('Не совпадают заголовки')

dfdf = (df_1.merge(df_2, how='outer', on=['Код изделия','Наименование изделия','Код сборки', 'Наименование сборки','Код компоненты','Наименование компоненты', 'Кол-во\nна\nсборку'],
              suffixes=['', '_new'], indicator=True))
dfdf2 = (df_2.merge(df_1, how='outer', on=['Код изделия','Наименование изделия','Код сборки', 'Наименование сборки','Код компоненты','Наименование компоненты', 'Кол-во\nна\nсборку'],
              suffixes=['', '_new'], indicator=True))


dfdf3=pd.merge(dfdf.query("_merge=='right_only'"), dfdf2.query("_merge=='right_only'"), how ='outer').drop_duplicates(subset=['Код изделия','Наименование изделия','Код сборки', 'Наименование сборки','Код компоненты','Наименование компоненты', 'Кол-во\nна\nсборку'])

print(dfdf3)