def calcular_impuesto(ingreso, tasa_impuestos):
    """
    Calcula el impuesto a pagar según el ingreso y la tasa de impuestos.
    """
    impuesto = ingreso * tasa_impuestos
    return impuesto

ingreso = float(input("Ingrese el ingreso: "))
tasa_impuestos = float(input("Ingrese la tasa de impuestos: "))

impuesto = calcular_impuesto(ingreso, tasa_impuestos)

print(f"El impuesto a pagar es: {impuesto:.2f}")