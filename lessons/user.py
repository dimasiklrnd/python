class User():
    """Класс пользователя"""

    def __init__(self, first_name, last_name, **other_info):
        """инициализация атрибутов"""
        self.first_name = first_name
        self.last_name = last_name
        self.other_info = other_info
        if self.other_info:  # если передано больше аргументов, то делаем словарь
            self.profile = {}
            self.profile['имя'] = self.first_name
            self.profile['фамилия'] = self.last_name
            for self.k, self.v in self.other_info.items():
                self.profile[self.k] = self.v
        self.login_attemts = 0

    def describe_user(self):
        """вывод персональной информации о пользователе"""
        if self.other_info:
            print('\n')
            for self.k, self.v in self.profile.items():
                print(self.k.title() + ': ' + self.v.title())

        else:
            print("\nИмя: " + self.first_name.title() +
                  '\n' + "Фамилия: " + self.last_name.title())

    def greet_user(self):
        """приветствие пользователя"""
        privet = '\nПриветствуем Вас, ' + self.first_name.title()+' ' + \
            self.last_name.title() + '!'
        print(privet)

    def increment_login_attemts(self):
        """ увеличивает значение (попытки входа) на 1 """
        self.login_attemts += 1
        # print(self.login_attemts)
        return self.login_attemts

    def reset_login_attemts(self):
        """ сбрасывает счетчик (попытки входа) на 0 """
        self.login_attemts = 0
        # print(self.login_attemts)
        return self.login_attemts
