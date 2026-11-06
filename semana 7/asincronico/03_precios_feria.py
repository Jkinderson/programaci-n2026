"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# Calcular promedio, mínimo, máximo y rango
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo

# Recorrer precios con while y contar los que superan el promedio
indice = 0
contador = 0

while indice < len(precios):
    if precios[indice] > promedio:
        contador += 1

    indice += 1

# Clasificar el rango
if rango >= 300:
    variacion = "Alta"
elif rango >= 150:
    variacion = "Moderada"
else:
    variacion = "Baja"

# Mostrar resultados
print("Producto:", producto)
print("Promedio: ₡", promedio)
print("Precio mínimo: ₡", minimo)
print("Precio máximo: ₡", maximo)
print("Rango: ₡", rango)
print("Precios sobre el promedio:", contador)
print("Variación:", variacion)
