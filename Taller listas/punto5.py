productos_orden = []
valor_total_orden = 0
num_productos = int(input("Ingrese el número de productos: "))

for i in range(num_productos):

    nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
    valor_bruto = float(input(f"Ingrese el precio de {nombre}: "))
    cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
    valor_neto = valor_bruto * cantidad

    valor_total_orden += valor_neto

    producto = {'nombre': nombre, 'precio_por_unidad': valor_bruto, 'cantidad': cantidad, 'valor_total': valor_neto}

    productos_orden.append(producto)


print(f"\n====== EL VALOR A PAGAR ES DE ${valor_total_orden} ====== ")
pago_cliente = float(input("Ingrese el pago: "))
devuelta = pago_cliente - valor_total_orden
print(f"\n El total del la orden fue {valor_total_orden:.2f} y su devuelta es de {devuelta:.2f}")
