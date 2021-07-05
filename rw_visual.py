import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Створювати нові блукання, доки програма активна
while True:
     # Створити випадкове блукання.
     rw = RandomWalk(5000)
     rw.fill_walk()

     # Нанести на графік точки блукання.
     plt.style.use('classic')
     fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

     point_numbers = range(rw.num_points)

     ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

     # Виокремити першу та останню точки.
     ax.scatter(0, 0, c='green', edgecolors='none', s=100)
     ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

     # Приховати осі.
     ax.get_xaxis().set_visible(False)
     ax.get_yaxis().set_visible(False)

     plt.show()

     keep_running = input('Згенерувати нове блукання? (y/n): ')
     if keep_running == 'n':
          break