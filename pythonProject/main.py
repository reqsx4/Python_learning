imie = input('Podaj imię: ')
print('Hello', imie)
if imie == 'Damian':
    print('ELOOO')
else:
    print('Kim jesteś?')

wiek = input('Ile masz lat?')
if int(wiek) >= 18:
    print('Jesteś dorosły')
else:
    ile = 18 - int(wiek)
    print('Musisz jeszcze poczekać', ile, 'lat')

#Operatory matematyczne
# + - suma
# - - różnica
# * - iloczyn
# / - iloraz
# % - modulo (reszta z dzielenia)
# // - dzielenie całkowito liczbowe 5//2 = 2

#Operatory logiczne
# > większy
# < mniejszy
# >= większy lub równy
# == równy
# != nierówny