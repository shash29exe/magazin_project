from magazines.shop import Shop
from magazines.magazines import Magazine
from magazines.user import ShopUser


def main():
    shop = Shop()
    mag1 = Magazine('Cosmopolitan', 'Hearst Corporation', 1886)
    mag2 = Magazine('National Geographic', 'Нейтан Ламп', 1888)
    shop.adder_magazines(mag1)
    shop.adder_magazines(mag2)

    user1 = ShopUser('Петя')
    shop.user_register(user1)

    print('Доступные журналы:')
    for i, mag in enumerate(shop.get_available_magazines()):
        print(f'{i+1}: {mag}')

    available = shop.get_available_magazines()
    print(user1.bought_magazine(available[0]))

    print(user1.return_magazine(available[0]))

if __name__ == '__main__':
    main()
