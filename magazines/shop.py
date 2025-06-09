class Shop:
    def __init__(self):
        self.magazines = []
        self.users = []

    def adder_magazines(self, magazine):
        self.magazines.append(magazine)
        return f'Получен журнал: {magazine}'

    def user_register(self, user):
        self.users.append(user)
        return f'Зарегистрирован пользователь: {user}'

    def list_available_magazines(self):
        available_magazines = [magazine for magazine in self.magazines if magazine.is_available]
        if len(available_magazines) <= 0:
            return 'Журналы отсутствуют.'

        return f'Доступные журналы:\n{available_magazines}'

    def get_available_magazines(self):
        return [magazine for magazine in self.magazines if magazine.is_available]