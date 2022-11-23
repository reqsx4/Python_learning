#Funkcje
def say_hello(first_name=''):
    print(f'Yo! {first_name}')

say_hello('Damian')
say_hello('Kamil')
say_hello('Twój stary')
say_hello()

def calculate_brutto(netto, vat=0.23):
    return netto + netto * vat

total = calculate_brutto(100)
total += calculate_brutto(700)
print(total)