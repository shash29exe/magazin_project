class ShopUser:
    def __init__(self, name):
        self.name = name
        self.buy_magazine = []

    def bought_magazine(self, magazine):
        if magazine.is_available:
            self.buy_magazine.append(magazine)
            magazine.is_available = False
            return f'Пользователь {self.name} купил журнал {magazine.title}'
        return f'{magazine.title} отсутствует в продаже'

    def return_magazine(self, magazine):
        if magazine in self.buy_magazine:
            self.buy_magazine.remove(magazine)
            magazine.is_available = True
            return f'Пользователь {self.name} вернул журнал {magazine.title}'
        return f'Пользователь {self.name} не имеет журнала {magazine.title}'

    def __str__(self):
        return f"Пользователь {self.name} имеет {', '.join([m.title for m in self.buy_magazine])}"