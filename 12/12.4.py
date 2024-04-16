import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных набора данных "penguins"
penguins = sns.load_dataset("penguins")

# Создание графика с помощью библиотеки Seaborn
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x="flipper_length_mm", y="body_mass_g", hue="species", data=penguins)
plt.title("Длина ласта и масса тела пингвинов")
plt.xlabel("Длина ласта (мм)")
plt.ylabel("Масса тела (г)")
plt.legend(title="Вид")
plt.show()