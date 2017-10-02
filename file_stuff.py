# f = open('blabla.txt', 'r+')
# content = f.read()
# f.write('\naaaaaaa')
# f.seek(0)
# content1 = f.read()
#
#
# print(content1)
# f.close()

# with open('blabla.txt', 'r') as f1:
#     content = f1.read()
# print('f1 inchis ', f1.closed)
#
# #above code simmilar to below
# # f = open ('')
# # content = f.read()
# # f.close()
# ##########################
#
# f2 = open ('output.txt', 'w+')
# f2.write(content)
# f2.seek(0)
# print(f2.read())
# f2.close()
# print('f2 inchis ', f2.closed)

with open('blabla.txt', 'r') as f:
    lines = f.readlines()

line2 = []
for line in lines:
    l = line.title()
    line2.append(l)

with open('output.txt', 'w+') as g:
    g.writelines(line2)
print
nrand = input('numar linie ')

#print(line2[int(nrand)])

rnd = line2[int(nrand)]
print(rnd)
n = input('numar index ')
print(rnd[int(n)])



