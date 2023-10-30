directorio_direc = {
    "Ele": "Roma 123, Italia",
    "Ju": "Paris 22a, Francia",
    "Pa": "Malaga 89, España"
}

print(directorio_direc["Ju"])
print(directorio_direc.get("Ja", "No existe en la base de datos"))

directorio_buscar = "Malaga 89, Españas"
if (directorio_buscar in directorio_direc.values()):
    for name, dire in directorio_direc.items():
        if (directorio_buscar == dire):
            print(name)
else:
    print("no existe la direccion indicada")
