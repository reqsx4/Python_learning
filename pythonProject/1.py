point_x = 1
point_y = 2

#tupla, krotka - niemutowalne (niezmienne)
point = 1, 2
print(point[0])
print(point[1])
# point[0] = 2 nie zadziała w tym przypadku
print(point)

# listy
cities = ['Torun', 'Bydgosz', 'Gdynia', 'Kijów']
print(cities[0])
print(cities[-1]) #od tyłu
cities.append('Warszawa')#po kropce są dodawane metody (takie jakby dodatkowe funkcje)
cities.append('Kraków')
print(cities)
cities.sort()
print(cities)
cities[-1] = 'Zakopane'
print(cities)

#słowniki
capitals = {
    'Poland': 'Warszawa',
    'France': 'Paris',
    'Germany': 'Berlin'
}
print(capitals['France'])

