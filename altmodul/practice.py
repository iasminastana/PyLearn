from coffee.machiato import grater_than
from fifi.pie import concatenate_list

def to_use():
    gg = grater_than(48, 549)
    lst1 = []
    lst2 = [98, 77]

    print('modul grater than {} '.format(gg))
    print('modul concatenate{} '.format(concatenate_list(lst1, lst2)))

if __name__ == '__main__':
    to_use()