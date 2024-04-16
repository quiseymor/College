import matplotlib.pyplot as plt

# Данные для построения диаграммы
labels = ['Роснефть', 'Сбербанк', 'ВТБ', 'Кузбассэнерго', 'Аэрофлот', 'АвтоВАЗ']
sizes = [35, 30, 15, 5, 10, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0', '#ffb3e6']

# Построение круговой диаграммы
plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Устанавливаем круговую форму диаграммы

plt.title('Структура инвестиционного портфеля')
plt.show()