peliculas = []

num_peliculas = int(input("Ingresa el número de peliculas a ingresar: "))


for i in range (num_peliculas):
    titulo = input(f"Ingresa el titulo de la película {i + 1}: ")
    genero = input(f"Ingresa el género de la película {titulo}: ")
    duracion_pelicula = input(f"Ingresa la duración de la película {titulo}: ")

    pelicula = {'Titulo': titulo, 'Genero': genero, 'Duracion_pelicula': duracion_pelicula}

    peliculas.append(pelicula)

print("\nLista de películas")

for pelicula in peliculas:
    print(f"{pelicula['Titulo']} / Género: {pelicula['Genero']} / Duración: {pelicula['Duracion_pelicula']}")


buscar_peli = input("Ingresa el título de la película que desas buscar: ")
encontrada = False

for pelicula in peliculas:
    if pelicula['Titulo'] == buscar_peli:
        print(f"La película {pelicula['Titulo']} del género {pelicula['Genero']} con la duración de {pelicula['Duracion_pelicula']} se encuentra.")
        encontrada= True
        break

if not encontrada:
    print(f"La película con el título '{buscar_peli}' no se encuentra en la lista.")

"""el pop elimina siempre el ultimo valor de una lista en caso de no darle un indiec"""
peliculas.pop()

print("\nLista de películas con la eliminación")
for pelicula in peliculas:
    print(f"{pelicula['Titulo']} / Género: {pelicula['Genero']} / Duración: {pelicula['Duracion_pelicula']}")





