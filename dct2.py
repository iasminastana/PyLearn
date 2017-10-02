#
d1 = {
    'a': 100,
    'b': 200,
    'c': 300

}
d2 = {
    'a': 50,
    'b': 35,
    'm': 36,
    'x': 555
}
df = {}
df.update(d1)
df.update(d2)
print(df)
for k, v in d1.items():
    for i, j in d2.items():
        if k == i:
            df[k] = v+j
print(df)

#same result
#df = d2
#
# if k in d2.keys():
#     if k in d1.keys():
#         df[k] = d1[k] + d2[k]
#     else:
#         df[k] = d2[k]
#


