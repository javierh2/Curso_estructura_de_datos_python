lista = [1, 2, 3, 4, 5]
max = 0

for num in lista:
    if max < num:
        max = num

print(max)

lista_negativa = [-1, -2, -3, -4, -5]
max = lista_negativa[0]

for num in lista_negativa:
    if max < num:
        max = num
print(max)
