capitals = {'USA': 'Washington, D.C.',
            'China': 'Beijing',
            'France': 'Paris',
            'England': 'London',
            'Italy': 'Rome',
            'Russia': 'Moscow',
            'Australia': 'Canberra',
            'Peru': 'Lima',
            'Japan': 'Tokyo'}

print('Iteração Direta:\n')

for country in capitals:
    print(f'{capitals[country]}, {country}')
print()

for country in capitals.keys():
    print(f'{capitals[country]}, {country}')
print()

for city in capitals.values():
    print(f'Capital city: {city}')
print()

for country, city in capitals.items():
    print(f'{city}, {country}')

print('\nChecando Membros')

print('England' in capitals)  # True
print('Lima' in capitals)  # checa as keys, por isso dá False

print('Moscow' in capitals.keys())  # False
print('Italy' in capitals.keys())  # True

print('Lima' in capitals.values())  # True
print('Houston' in capitals.values())  # False
