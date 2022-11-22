unconfirmed_users = ['alice', 'brian', 'candace'] # пользователей для проверки
confirmed_users = ['shevchenko', 'vadim'] # и списка для хранения проверенных пользователей.
# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку, перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Перевірка користувача: " + current_user.title())
    confirmed_users.append(current_user)
# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())