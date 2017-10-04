import math


class Coffee:

    def __init__(self, coffee_spoons, sugar, water):
        self.coffee_spoons = coffee_spoons
        self.sugar = sugar
        self.water = water

    def prepare_coffee(self):
        cantitate_totala_cafea = 2*self.coffee_spoons + self.sugar + 4*self.water
        return cantitate_totala_cafea

    def prepare_time_coffee(self):
        time2prepare = self.water / (math.sin(math.pi/2) * math.cos(math.pi)) * self.coffee_spoons
        print(f'Time to prepare:{time2prepare}')
