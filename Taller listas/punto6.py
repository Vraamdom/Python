agenda_telefonica = {}

while True:
  print("\nMenú:")
  print("1. Agregar contacto")
  print("2. Buscar número de teléfono")
  print("3. Salir")

  opcion = input("Ingrese su opción: ")

  if opcion == "1":
    nombre = input("Ingrese el nombre del contacto: ")
    numero_telefono = input("Ingrese el número de teléfono: ")
    agenda_telefonica[nombre] = numero_telefono
    print("Contacto agregado.")
  elif opcion == "2":
    nombre_buscado = input("Ingrese el nombre de la persona a buscar: ")
    if nombre_buscado in agenda_telefonica:
      print(f"El número de teléfono de {nombre_buscado} es: {agenda_telefonica[nombre_buscado]}")
    else:
      print(f"No se encontró el número de teléfono de {nombre_buscado}.")
  elif opcion == "3":
    break
  else:
    print("Opción inválida.")

print("\n¡Gracias por usar la agenda telefónica!")
