def calcular_precio_total(precio_unidad, cantidad, precio_minimo_descuento=120000):
  if precio_unidad < 0 or cantidad < 0:
    raise ValueError("Los valores de precio y cantidad deben ser números positivos.")

  precio_total = precio_unidad * cantidad

  if precio_total >= precio_minimo_descuento:
    descuento = precio_total * 0.1
    precio_total -= descuento

  return precio_total

precio_unidad = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos a comprar: "))

precio_total = calcular_precio_total(precio_unidad, cantidad)
print(f"El precio total de la compra es de: {precio_total:.2f}")
