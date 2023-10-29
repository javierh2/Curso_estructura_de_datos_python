matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [2, 4, 6, 9]
]

print(matriz[2][1])
print(matriz)

# recorrido 1
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print(" ")


# recorrido 2
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()