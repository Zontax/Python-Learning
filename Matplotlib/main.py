import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gsc
# Тест три різних графіка на одному полотні з одими данними
# plt.style.use('seaborn-whitegrid') # Стиль

x1 = [0, 1, 2, 3]
y1 = [a * a for a in x1]

ax1 = plt.subplot(131)
plt.plot(x1, y1, 'r--')  # o,s- точка, r - колір, -- декоратор
plt.fill_between(x1, y1)
plt.grid()

ax2 = plt.subplot(132)
plt.plot(x1, y1, 'go-')
plt.fill_between(x1, y1)
plt.grid()

ax3 = plt.subplot(133)
plt.plot(x1, y1, 'yo-.')
plt.grid()

# Відображення вікна
plt.show()
