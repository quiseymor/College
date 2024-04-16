import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из csv файлов
sberbank_data = pd.read_csv('sberbank_2023.csv')  # файл с данными по акциям Сбербанка
rosneft_data = pd.read_csv('rosneft_2023.csv')    # файл с данными по акциям Роснефти

# Выбираем только столбец с ценами закрытия
sberbank_close = sberbank_data['CLOSE']
rosneft_close = rosneft_data['CLOSE']

# Коррелограмма (диаграмма рассеяния)
plt.scatter(sberbank_close, rosneft_close)
plt.title('Коррелограмма цен на акции Сбербанка и Роснефти')
plt.xlabel('Цены закрытия акций Сбербанка')
plt.ylabel('Цены закрытия акций Роснефти')
plt.show()

# Линия регрессии
coef = np.polyfit(sberbank_close, rosneft_close, 1)
poly1d_fn = np.poly1d(coef) 
plt.plot(sberbank_close, poly1d_fn(sberbank_close), color='red')
plt.scatter(sberbank_close, rosneft_close)
plt.title('Линия регрессии и коррелограмма цен на акции Сбербанка и Роснефти')
plt.xlabel('Цены закрытия акций Сбербанка')
plt.ylabel('Цены закрытия акций Роснефти')
plt.show()

# Расчет коэффициента корреляции
correlation = np.corrcoef(sberbank_close, rosneft_close)[0, 1]
print(f"Коэффициент корреляции: {correlation}")