inventario = {}

while True:
  print("\nMenú:")
  print("1. Agregar producto")
  print("2. Actualizar stock")
  print("3. Mostrar stock de un producto")
  print("4. Salir")

  opcion = input("Ingrese su opción: ")

  if opcion == "1":
    nombre_producto = input("Ingrese el nombre del producto: ")
    stock_producto = int(input("Ingrese el stock del producto: "))
    inventario[nombre_producto] = stock_producto
    print("Producto agregado.")
  elif opcion == "2":
    nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
    if nombre_producto in inventario:
      accion = input("¿Agregar o quitar stock? (a/q): ")
      if accion.lower() == "a":
        cantidad_stock = int(input("Ingrese la cantidad a agregar: "))
        inventario[nombre_producto] += cantidad_stock
      elif accion.lower() == "q":
        cantidad_stock = int(input("Ingrese la cantidad a quitar: "))
        inventario[nombre_producto] -= cantidad_stock
        if inventario[nombre_producto] < 0:
          print("¡Error! El stock no puede ser negativo.")
          inventario[nombre_producto] += cantidad_stock  # Revierte la operación
      else:
        print("Acción inválida.")
    else:
      print(f"No se encontró el producto {nombre_producto} en el inventario.")
  elif opcion == "3":
    nombre_producto = input("Ingrese el nombre del producto a mostrar: ")
    if nombre_producto in inventario:
      print(f"El stock actual de {nombre_producto} es: {inventario[nombre_producto]}")
    else:
      print(f"No se encontró el producto {nombre_producto} en el inventario.")
  elif opcion == "4":
    break
  else:
    print("Opción inválida.")

print("\n¡Gracias por usar el sistema de inventario!")