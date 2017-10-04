from caffe.cafelatte import Caffelatte
from caffe.ciocolata import Coffee


if __name__ == '__main__':
    espresso = Coffee(coffee_spoons=3, sugar=1, water=6)
    latte = Caffelatte(milk=5, coffee_spoons=2, sugar=2, water=4)

    print(f'Prepare coffee espreso {espresso.prepare_coffee()}')
    espresso.prepare_time_coffee()
    print(f'Prepare coffee late {latte.prepare_coffee()}')
    latte.prepare_time_coffee()
    print(f'Energy {latte.energy()}')
