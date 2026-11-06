"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
total = sum(consumos_litros)
promedio = total / len(consumos_litros)

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]
ahorro = primer_dia - ultimo_dia
reduccion = (ahorro / primer_dia) * 100 if primer_dia != 0 else 0

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
if reduccion >= 15:
    clasificacion = "Reducción alta"
elif reduccion > 0:
    clasificacion = "Reducción moderada"
else:
    clasificacion = "Sin reducción"
    
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.


print("Consumo total:", total, "L")
print("Promedio diario:", promedio, "L")
print("Litros ahorrados:", ahorro, "L")
print("Porcentaje de reducción:", reduccion, "%")
print("Clasificación:", clasificacion)