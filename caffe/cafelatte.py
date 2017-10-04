import math
from .ciocolata import Coffee


class Caffelatte(Coffee):

    def __init__(self, coffee_spoons, sugar, water, milk):
        super().__init__(coffee_spoons, sugar, water)
        self.milk = milk

    def energy(self):
        energy = self.milk * self.coffee_spoons ^ 2
        return energy

    def prepare_coffee(self):
        cantitate_totala_cafea = super().prepare_coffee() + self.milk
        return cantitate_totala_cafea

    def prepare_time_coffee(self):
        time2prepare = self.water / (math.sin(math.pi / 2) * math.cos(math.pi)) * self.coffee_spoons + self.milk
        print(f'Time to prepare:{time2prepare}')
