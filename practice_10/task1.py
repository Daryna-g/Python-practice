import numpy as np
import matplotlib.pyplot as plt

# Створюємо масив значень x у діапазоні [-3, 3]
x = np.linspace(-3, 3, 1000)

# Обчислюємо y(x) = 2^x * sin(10x)
y = (2**x) * np.sin(10 * x)

# Побудова графіка
plt.plot(x, y, color="red", linewidth=2,
         linestyle="-", label="y(x) = 2^x * sin(10x)")

plt.xlabel("Вісь X")
plt.ylabel("Вісь Y")

plt.title("Графік функції y(x) = 2^x * sin(10x)")

plt.grid(True)

plt.legend()

plt.show()
