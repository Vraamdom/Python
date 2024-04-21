calificaciones = []

num_estudiantes = int(input("Ingrese el número de estudiantes: "))

for i in range(num_estudiantes):

    nombre = input(f"Ingrese el nombre del esttudiante {i + 1}: ")
    nota1 = float(input(f"Ingrese la nota 1 del estudiante {nombre}: "))
    nota2 = float(input(f"Ingrese la nota 2 del estudiante {nombre}: "))
    nota3 = float(input(f"Ingrese la nota 3 del estudiante {nombre}: "))
    promedio = (nota1 + nota2 + nota3)/3

    estudiante = {'nombre': nombre, 'nota1': nota1, 'nota2': nota2, 'nota3':nota3, 'promedio':promedio}

    calificaciones.append(estudiante)

print("\nLista de calificaciones:")

for calificion in calificaciones:
    print(f"{calificion['nombre']} / Nota 1: ${calificion['nota1']} / Nota 2: {calificion['nota2']} / Nota 3: {calificion['nota3']}/ Promedio: {calificion['promedio']:.1f}")
