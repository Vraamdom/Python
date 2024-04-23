palabras_prohibidas = ["brandon", "grosero", "insulto", "basura"]

while True:
  mensaje = input("Ingrese un mensaje: ")
  mensaje_censurado = mensaje

  for palabra_prohibida in palabras_prohibidas:
    if palabra_prohibida in mensaje:
      mensaje_censurado = mensaje_censurado.replace(palabra_prohibida, "*" * len(palabra_prohibida))

  if mensaje_censurado != mensaje:
    print(f"Mensaje censurado: {mensaje_censurado}")
  else:
    print(f"El mensaje no contiene palabras prohibidas: {mensaje}")
