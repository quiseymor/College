import json
import matplotlib.pyplot as plt

with open('population_data.json', 'r') as file:
    data = json.load(file)

country_name = "Arab World"
filtered_data = [entry for entry in data if entry["Country Name"] == country_name]

# Строим график
years = [int(entry["Year"]) for entry in filtered_data]
population_values = [float(entry["Value"]) for entry in filtered_data]

plt.figure(figsize=(12, 6))
plt.plot(years, population_values, marker='o', linestyle='-')
plt.title(f"Изменение численности населения страны {country_name} (1960-2010)")
plt.xlabel("Год")
plt.ylabel("Численность населения")
plt.grid(True)
plt.show()
