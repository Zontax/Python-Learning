current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: # якщо залишок від ділення 0 перейти у початок циклу
        continue
    print(current_number)