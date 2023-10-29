tupla = ("a", "b", "c", "d")

tupla_2 = 1, 2, 3, 4

tupla_comb = ("a", 2, "b", 4.4)
print(tupla)
print(tupla_comb)
print(tupla_2)
print(tupla_comb[1])
print("\n")

tupla_grande = ("py", "php", "js", "ruby", "go", "c#")

for tupla in tupla_grande:
    print(tupla)

print(tupla_grande[2:])
print("\n")

print(tupla_grande)
lista_grande = list(tupla_grande)
print(lista_grande)
print(type(lista_grande))
print(type(tupla_grande))


lista_bjj = ["atama", "vital", "keiko", "vouk"]
print(lista_bjj)
print(type(lista_bjj))

tupla_bjj = tuple(lista_bjj)
print(tupla_bjj)
print(type(tupla_bjj))

# recorrer una tupla

for kimono in tupla_bjj:
    print(kimono)
