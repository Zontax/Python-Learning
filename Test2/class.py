class Point:
    "Опис класа Point"
    color = 'red'
    circle = 2

    def set_one(self):
        print("It's " + str(self))

    def __init__(self):
        print()

a = Point()  # Об'єкт класа
a.set_one()  # Визов метода об'єктом класа

print(getattr(Point, 'color'))
print(hasattr(Point, 'city'))
print(delattr(Point, 'color'))
print(Point.__doc__)
