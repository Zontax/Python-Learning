class Dog():
    """Простая модель собаки"""
    def __init__(self, name, age): # Метод __init__
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        return self.name.title() + " зараз сидить."

    def roll_over(self):
        """Собака перекатывается по команде."""
        return self.name.title() + " перекинувся!"

my_dog = Dog('бобік', 5) # Екземпляр класса
you_dog = Dog('патрон', 8)
print("Мою собаку звуть " + my_dog.name.title() + ".\nЙому " + str(my_dog.age) + " років.")
print(my_dog.sit())
print(you_dog.roll_over())
