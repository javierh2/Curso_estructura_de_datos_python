lista = ["g", "f", "e", "d", "c", "b", "a"]
nueva_lista = []

for indice in range(len(lista)-1, -1, -1):
    nueva_lista.append(lista[indice])
print(nueva_lista)
