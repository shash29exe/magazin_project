class Magazine:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.is_available = True

    def __str__(self):
        return f'Журнал: {self.name} под авторством {self.author}, {self.year} года издательства'

