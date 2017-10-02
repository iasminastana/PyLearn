l = []

# print(type(l))
#
# print(len(l))

l.append('abc')
l.append([1, 2])
l.append(6)
l.append(5)

l.extend([1, 4, 5, 6, ])

# print('marime', len(l))
#
# print('element2:', l[1])
#print(l)
# print('de la elm 4 pana la sf:', l[3:])
#
# print(l[-1])
# print(l[-2:])
# print(l[2:3])

# cuvant = 'gigi are prune'
#
# print(cuvant[-5:])
# print(cuvant[-6:])
# print(cuvant.split(' '))
# print(l.index(5))

# for item in l:
#     tipul = type(item)
#     print(f'{type(item)}')
#     print(f'{tipul.__name__}')

# if 'a' in l:
#     print('a')
# elif 5 not in l:
#     print('b')
# else:
#     print('go home')

m = []
for item in l:
    if type(item) == int:
        m.append(item)
print(m)

m.reverse()
print(m)
print(l)
while True:
    print('a')
    break
while 1 in l:
    a = l.pop(2)
    print(a)

new_list = []
for i in l:
    if type(i) == int:
        new_list.append(i)
int_list = [i for i in l if type(i) == int]






