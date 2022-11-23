#Pętle

#for - skończona/określona ilość razy (ilość elementów, range())

for n in range(10):
    print(n)

for _ in range(10):
    print('Potężna loopa')

#while - wykonuje się dopóki twierdzenie jest prawdziwe
numbers = 0
while int(numbers) < 30:
    entries = int(input('Ile osób wchodzi?'))
    numbers += entries

    print('Razem', numbers)