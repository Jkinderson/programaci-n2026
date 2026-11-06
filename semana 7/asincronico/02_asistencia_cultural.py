"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
# TODO: Calcule el promedio y su porcentaje de ocupación.
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
total = 0
cantidad_bloques = 0

for asistencia in asistencias:
    total += asistencia

    if asistencia > capacidad * 0.70:
        cantidad_bloques += 1

# Calcular promedio y porcentaje de ocupación
promedio = total / len(asistencias)
porcentaje = (promedio / capacidad) * 100

# Clasificar el promedio
if porcentaje >= 80:
    estado = "Ocupación alta"
elif porcentaje >= 50:
    estado = "Ocupación media"
else:
    estado = "Ocupación baja"

# Mostrar resultados
print("Total de asistentes:", total)
print("Promedio de asistentes:", promedio)
print("Porcentaje de ocupación:", porcentaje, "%")
print("Cantidad de bloques que superan el 70 %:", cantidad_bloques)
print("Estado:", estado)