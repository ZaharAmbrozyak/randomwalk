import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Створювати нові блукання, доки програма активна
while True:
     # Створити випадкове блукання.
     rw = RandomWalk()
     rw.fill_walk()

     # Нанести на графік точки блукання.
     plt.style.use('classic')
     fig, ax = plt.subplots()

     point_numbers = range(rw.num_points)

     point_size = 0.003*rw.num_points
     ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=point_size)

     # Виокремити першу та останню точки.
     point_size_extreme = point_size*6.66
     ax.scatter(0, 0, c='green', edgecolors='none', s=point_size_extreme)
     ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=point_size_extreme)

     # Приховати осі.
     ax.get_xaxis().set_visible(False)
     ax.get_yaxis().set_visible(False)

     plt.show()

     keep_running = input('Згенерувати нове блукання? (y/n): ')
     if keep_running == 'n':
          break