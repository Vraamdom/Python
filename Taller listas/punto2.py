libros_prestados = []

num_libros_prestados = int(input("Ingresa el número de libro pestados a ingresar: "))

for i in range (num_libros_prestados):
    titulo_libro = input(f"Ingresa el titulo del libro prestado {i + 1}: ")
    fecha_devolucion = input(f"Ingresa la fecha en la que devuelves el libro {titulo_libro}: ")

    libro_devuelto = {'Titulo': titulo_libro, 'Fecha_devolucion': fecha_devolucion}

    libros_prestados.append(libro_devuelto)

print("\nLista de libros prestados")

for libro in libros_prestados:
    print(f"{libro['Titulo']} / Fecha devolución: {libro['Fecha_devolucion']}")

