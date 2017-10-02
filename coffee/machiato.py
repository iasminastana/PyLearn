def grater_than(a, b):
    """
    :param a: is an int
    :param b: is an int
    :return: turns true if a>b
    """
    if a > b:
        return True
    return False

if __name__ == '__main__':
    gt = grater_than(3, 5)
    print('machiato {}'.format(gt))
