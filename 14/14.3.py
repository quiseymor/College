import requests
import pygal
from collections import Counter

url = 'https://api.github.com/users/quiseymor/repos'
response = requests.get(url)
repos = response.json()

#ЯП
languages = [repo['language'] for repo in repos if repo['language']]
languages_counter = Counter(languages)

# создание
months = [repo['created_at'] for repo in repos]
month_counter = Counter([month.split('-')[1] for month in months])
weekday_counter = Counter([month.split('-')[2].split('T')[0] for month in months])

bar_chart = pygal.Bar()
bar_chart.title = 'Языки программирования в репозиториях аккаунта'
bar_chart.x_labels = languages_counter.keys()
bar_chart.add('Количество проектов', languages_counter.values())
bar_chart.render_in_browser()

bar_chart_weekday = pygal.Bar()
bar_chart_weekday.title = 'Количество проектов, созданных по дням недели'
bar_chart_weekday.x_labels = weekday_counter.keys()
bar_chart_weekday.add('Проекты', weekday_counter.values())
bar_chart_weekday.render_in_browser()



print("Общее количество репозиториев:", len(repos))
print("Список всех языков программирования:", set(languages))
print("Количество проектов для каждого языка программирования:", (languages_counter))
print("Информация о днях создания репозиториев по месяцам:", month_counter)
print("Информация о днях создания репозиториев по дням недели:", weekday_counter)
