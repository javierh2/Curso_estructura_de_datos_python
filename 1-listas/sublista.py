lista = ["a", "b", "c"]
lista_distinta = ["a", 2, 4.4, "b", "D"]
lista_1 = list()

print(lista_distinta[1])     # accediendo a un elemento de la lista por su indice
print(lista_distinta[:2])
lista[1] = "B"      # modificando un elemento de la lista
print(lista)


# sublista
lista_grande = ["py", "js", "php", "java", "c++", ".net"]
lista_menor = lista_grande[0:3]     # inicio y limite del rango
print(lista_menor)
