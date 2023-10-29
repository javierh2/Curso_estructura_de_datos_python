# lista = [1, 2]
# lista.append(3)     # añadiendo un elemento a la lista .append
# print(lista)

# lista.extend([4, 5, 6])      # añade una sublista que se anexa a la lista original
# print(lista)
# # print(id(lista))

# lista.insert(2, "ultraviolento")      # agregar un elemento en una ubicacion especifica (2 parametros indice-valor)
# print(lista)
# # print(id(lista))

# # eliminar datos por 2 metodos

# letras = ["x", "y", "z"]
# # print(id(letras))
# letras.remove("x")      # se elimina la primera ocurrencia encontrada con el mismo valor
# print(letras)
# # print(id(letras))
# letras.insert(0, "x")
# letras.extend(["x", "y", "z"])
# print(letras)
# letras.remove("x")
# print(letras)

# letras.pop(0)       # elimina el elemento del indice
# print(letras)


numeros = [1, 2, 2, 2, 2, 2, 3, 4, 5]
print(numeros.count(2))     # cuenta ocurrencias de un elemento

colores = ["blanco", "azul", "morado", "marron", "negro"]      # devuelve posicion en base a un elemento
print(colores.index("azul"))
print(len(colores))      # cantidad de elementos que forman parte de la lista
