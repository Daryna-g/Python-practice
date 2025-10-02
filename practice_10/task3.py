import matplotlib.pyplot as plt

# Дані (в тис. осіб)
labels = ['0–4 роки', '5–9 років', '10–14 років', '15–17 років']
values = [1566.8, 2221.6, 2331.5, 1228.6]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(values,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0.05, 0.05, 0.05, 0.05))

plt.title('Розподіл дітей за віковими групами в Україні (2022 р.)')
plt.axis('equal')
plt.show()
