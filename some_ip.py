import requests

response = requests.get('https://httpbin.org/ip')

# print('Your IP is {0}'.format(response.json()['origin']))

org = response.json()['origin']

print(f'Your IP is {org}')

