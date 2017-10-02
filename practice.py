citesc1 = input('citesc1: ')
citesc2 = input('citesc2: ')
suma = 0
for i in citesc1:
    if i.isdigit():
        suma += int(i)
for i in citesc2:
    if i.isdigit():
        suma += int(i)

print(suma)
