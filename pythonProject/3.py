#Zbiory (rzeczy w nich się nie powtarzają i kolejność nie jest uwzględniania)
capitals = {'Warsaw', 'London', 'Paris'}
capitals = set(['Warsaw', 'London', 'Paris', 'Warsaw'])
loved ={'Toruń', 'London'}

print(capitals)
print(loved)

#Odejmowanie zbiorów
print(capitals - loved)
#Część wspólna
print(capitals & loved)
#Rozłączność
print(capitals ^ loved)