# Завдання 1
users_age = {"Anna": "baby",
             "Bohdan": "child",
             "Oleg": "teenager",
             "Mary": "adult",
             "Mykhailo": "pensioners"}
try:
    found_user = input("Введіть своє ім'я:")
    print(users_age[found_user])
except KeyError:
    print("Такого користувача не існує")

# Завдання 2

try:
    user_number = input("Введіть число:")
    number = int(user_number)
    print("Введіть число:", number)
except ValueError:
    print("Ваше число не можливо конвертувати")