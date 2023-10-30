lenguajes = {"py", "php", "js"}
bdd = {"mysql", "sqlite", "mariadb", "py"}


full = lenguajes.union(bdd)
print(full)

coincidencias = lenguajes.intersection(bdd)
print(coincidencias)

print(lenguajes.isdisjoint(bdd))

mas_lenguajes = {"java", "ruby", "py"}
print(lenguajes.isdisjoint(mas_lenguajes))


print(lenguajes.difference(mas_lenguajes))
