import json
# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'lessons/files_and_exceptions/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'lessons/files_and_exceptions/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
