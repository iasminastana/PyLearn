smt = input('Write something: ')
letters = 0
digit = 0
for c in smt:
    if c.isalpha():
        letters += 1
    elif c.isnumeric():
        digit += 1
print('DIGITS: ', digit, ' CHARS: ', letters)
