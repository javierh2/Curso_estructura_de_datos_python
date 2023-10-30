lista_alumnos = [
    {"nombre": "Ele", "apellido": "Tro", "id": 123, "cursos": ["html", "js", "css"]},
    {"nombre": "Ju", "apellido": "Arc", "id": 456, "cursos": ["html", "boot", "tail"]},
    {"nombre": "Fri", "apellido": "Kal", "id": 789, "cursos": ["java", "php", "py"]}
]

lista_alumnos[2]["cursos"].pop(1)
print(lista_alumnos[2])
