def concatenate_list(a, b):
    """
    concatenate two lists
    """
    a.extend(b)
    return a

if __name__ == '__main__':
    l1 = [2, 3, 5]
    l2 = [4, 6, 7]
    n1 = concatenate_list(l1, l2)
    print('pie{}'.format(n1))