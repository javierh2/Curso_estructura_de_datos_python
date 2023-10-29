# sumatoria de una lista

lista = [2, 4, 6, 1, 2]
sumatoria = 0

for num in lista:
    sumatoria += num

print(sumatoria)


promedio = 0

for num in lista:
    promedio += num

promedio /= len(lista)
print(promedio)
