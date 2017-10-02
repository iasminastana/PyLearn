class AtLeast:
    """"
    Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Hints: Use init method to construct some parameters
    """

    def __init__(self, cit,):#de cate ori sa ia de la tastatura
        self.cit = cit
        self.unstr = ''

    def getString(self):

        for i in range(self.cit):
          self.unstr += input('citesc de la tastatura: ') + ' '

        self.unstr = self.unstr[:-1] + '.'

    def printString(self):

         print(self.unstr.upper())


if __name__ == '__main__':
    ts = AtLeast(5)
    ts.getString()
    ts.printString()


