from user import Admin

имя = input("Введите ваше имя: ")
фамилия = input("Ваша фамилия: ")

флаг = True
while флаг:
    вопрос = input("Желаете ввести другие данные? (д/н): ")
    if вопрос == 'д' or 'н':
        флаг = False

другое = {}

if вопрос == 'д':
    print('\n\tВводите сначала атрибут, а на следующей строке - значение.\n\n\t\t__!!! По завершении введите "конец" !!!___')

    active = True
    while active:
        key = input("\nатрибут: ")
        if key == 'конец':
            active = False
            continue

        value = input("значение: ")
        if value == 'конец':
            active = False
            continue

        другое[key] = value

    user1 = Admin(имя, фамилия, **другое)
    user1.describe_user()
    user1.greet_user()
    user1.show_privileges()

else:
    user1 = Admin(имя, фамилия)
    user1.describe_user()
    user1.greet_user()
    user1.show_privileges()
