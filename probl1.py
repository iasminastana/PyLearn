i = 0
l = []
for i in range(2000, 3200):
    if i % 7 == 0:
        if i % 5 != 0:
            l.append(i)
            i += 1

print(*l, sep=', ')
