
class Fruit:

    """
     this is a fruit class
    """
    VARIABILE = 5

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def _gigi(self):
        print('is private')

    def show(self):
        print(f'This fruit is {self.color} and is named {self.name}')
        self._gigi()

    @staticmethod
    def apb(a, b):
        return a+b

if __name__ == '__main__':
    plum = Fruit('plum', 'purple')
    apple = Fruit('IAplle', 'red')

    plum.show()
    apple.show()
    plum._gigi()

    print(Fruit.apb(2, 5)) #apelezi direct
    print(plum.apb(2, 5))
    print(plum)


    # print(plum.__dict__)
    # print(plum.__doc__)
