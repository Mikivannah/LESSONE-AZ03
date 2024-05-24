#  Создай гистограмму для случайных данных, сгенерированных с помощью функции numpy.random.normal.# # Параметры нормального распределения
# mean = 0       # Среднее значение
# std_dev = 1    # Стандартное отклонение
# num_samples = 1000  # Количество образцов
#Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)
##
# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных
# с помощью функции numpy.random.rand.
#
# import numpy as np
#
# random_array = np.random.rand(5)  # массив из 5 случайных чисел
# print(random_array)

import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Гистограмма для случайных данных, распределенных по нормальному закону')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

# Генерация двух наборов случайных данных для диаграммы рассеяния
num_points = 100
x_data = np.random.rand(num_points)
y_data = np.random.rand(num_points)

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 5))
plt.scatter(x_data, y_data, alpha=0.7, edgecolors='w', s=100)
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()