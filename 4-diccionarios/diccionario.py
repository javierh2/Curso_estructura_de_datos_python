estudiante = {
    "nombre": "Juan",
    "apellido": "Mora",
    "edad": 34,
    "ciudad": "Oslo"
}

print(estudiante["nombre"])

estudiante["edad"] = 36
print(estudiante)

estudiante["cursos"] = ["python", "java", "docker", "nodejs"]
print(estudiante)

# for key in estudiante:
#     print(key)

# for valor in estudiante:
#     print(estudiante[valor])

for llave, valor in estudiante.items():
    print(llave, ": ", valor)
