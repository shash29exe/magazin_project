class Magazine:
    """
        Класс для описания журнала.
    """

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def __str__(self):
        return f'Журнал: {self.title} под авторством {self.author}, {self.year} года издательства'
