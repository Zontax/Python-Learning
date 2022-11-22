from random import randint

class Die():
    """Простая модель собаки"""
    def __init__(self, sides=6): # Метод __init__
        """Инициализирует атрибуты name и age."""
        self.sides = sides

    def roll_die(self):
        for i in range(10):
            print(randint(1, self.sides))
         
cube_6 = Die()

print(cube_6.roll_die())

cube_10 = Die()

cube_20 = Die()