import matplotlib.pyplot as plt
import datetime

dates = []
users = []
with open('data.txt', 'r') as file:
    next(file)  # пропускаем первую строку (заголовки столбцов)
    for line in file:
        data = line.split()
        dates.append(datetime.datetime.strptime(data[1], '%d-%m-%Y'))
        users.append(int(data[2]))

# Рассчет динамики количества пользователей на каждую дату нарастающим итогом
cumulative_users = []
total = 0
for user in users:
    total += user
    cumulative_users.append(total)


fig1_label = "Фигура 1"
fig2_label = "Фигура 2"

# Построение графика для ежемесячных подключений
#plt.figure(figsize=(10, 5))
plt.subplot(2,2,1)
plt.plot(dates, users, label='Ежемесячные подключения')
plt.xlabel('Дата')
plt.ylabel('Количество пользователей')
plt.title('Динамика подключения абонентов интернет-провайдера (ежемесячные подключения)')
plt.legend()
plt.grid(True)


# Построение графика для изменения количества пользователей нарастающим итогом
#plt.figure(figsize=(10, 5))
plt.subplot(2,2,3)
plt.plot(dates, cumulative_users, label='Изменение количества пользователей нарастающим итогом')
plt.xlabel('Дата')
plt.ylabel('Количество пользователей')
plt.title('Динамика подключения абонентов интернет-провайдера (нарастающим итогом)')
plt.legend()
plt.grid(True)

plt.show()