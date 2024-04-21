productos = []

num_productos = int(input("Ingrese el número de productos: "))

for i in range(num_productos):

    nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))

    producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}

    productos.append(producto)

print("\nLista de Productos:")

for producto in productos:
    print(f"{producto['nombre']} / Precio: ${producto['precio']:.2f} / Cantidad: {producto['cantidad']}")
