nb = input('Write something ')

lst = sorted(nb.split(","))

newls = ",".join(lst)

print('You wrote %s \n' % newls.lower())

lst.reverse()

newls = ",".join(lst)

print('You wrote %s \n' % newls.upper())


