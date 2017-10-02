d = {
    'key': 'val',
    'key2': 'val2',
    'a': 2,
}
d['key3'] = 'val'

print(d)
print(d.keys())
print(d.items())

for k, v in d.items():
    print('{} > {}'.format(k, v))