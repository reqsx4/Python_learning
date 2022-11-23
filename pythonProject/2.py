from random import choice

#słowniki
capitals = {
    'Poland': 'Warszawa',
    'France': 'Paris',
    'Germany': 'Berlin'
}

selected = choice(list(capitals.keys()))

odpowiedz = input(f'Jaka jest stolica {selected}?')
if odpowiedz == capitals[selected]:
    print('Doobrzee')
else:
    print('No tak średnio bym powiedział, chyba miałeś na myśli', capitals[selected])

