class Restauran():
    """Клас моделі ресторану"""
    def __init__(self,  restaurant_name, cuisine_type): # Метод __init__
        """Ініціалізує атрибути restaurant_name и cuisine_type."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        '''Виводить данні про ресторан'''
        return f'Назва: {self.restaurant_name}\nКухня: {self.cuisine_type}'

    def open_restaurant(self):
        '''Виводить данні'''
        return f'Ресторан {self.restaurant_name} відкритий\n'

    def set_number_served(self, number): 
        '''Встанювлює певну к-сть відвідувачів'''
        self.number_served = number
    def update_served(self, number):
        if mileaччччge >= self.number_served:
            self.number_served = mileage
        else:
            print("You can't roll back an odometer!")

    def read_number_served(self):
        '''читає к-сть відвідувачів'''
        return str(self.number_served)

china_r = Restauran('китайський', 'китайська') # Екземпляр ресторану 'Китайський'
berezevskiy_r = Restauran('беревевський', 'українська') # Екземпляр ресторану 'Китайський'

print(china_r.describe_restaurant()+'\n'+china_r.open_restaurant() + str(china_r.number_served))
print(berezevskiy_r.describe_restaurant()+'\n'+berezevskiy_r.open_restaurant() + str(berezevskiy_r.number_served))
china_r.number_served = 5 # Зміна значення атрибуту number_served напряму
china_r.set_number_served(15)
print(china_r.read_number_served())