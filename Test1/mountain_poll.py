responses = {}
# Установка флага продолжения опроса.
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ") # Запрос имени и ответа пользователя.
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response # Ответ сохраняется в словарe
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Опрос завершен, вывести результаты.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
    # Проверка продолжения опроса.