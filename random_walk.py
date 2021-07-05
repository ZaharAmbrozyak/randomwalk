from random import choice

class RandomWalk:
     """Клас, що генерує випадкові блукання."""

     def __init__(self, num_points=5000):
          """Ініціалізувати атрибути блукання."""

          self.num_points = num_points

          # Всі блукання починаються з (0, 0).
          self.x_values = [0]
          self.y_values = [0]

     def get_step(self):
          direction = choice([1, -1])
          distance = choice(range(0,5))
          return direction * distance

     def fill_walk(self):
          """Обчислити всі точки блукання."""

          # Продовжувати робити кроки, доки блукання не досягне необхідної
          # довжини.
          while len(self.x_values) < self.num_points:

               # Вирішити, в якому напрямку рухатися та як довго
               x_step = self.get_step()
               y_step = self.get_step()

               # Відкинути кроки, що нікуди не просуваються.
               if x_step == 0 and y_step == 0:
                    continue

               # Розрахувати нову позицію.
               x = self.x_values[-1] + x_step
               y = self.y_values[-1] + y_step

               self.x_values.append(x)
               self.y_values.append(y)
