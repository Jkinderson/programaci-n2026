"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]

meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.

total_centro = sum(ventas_centro) #total de venta semanal
cantidad_centro = len(ventas_centro) #len cuenta las cantidades

menor_centro = min(ventas_centro)
mayor_centro = max(ventas_centro)
promedio_centro = total_centro / cantidad_centro
porcentaje_centro = total_centro * 100 / meta_centro


total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)
menor_norte = min(ventas_norte)
mayor_norte = max(ventas_norte)
promedio_norte = total_norte / cantidad_norte
porcentaje_norte = total_norte * 100 / meta_norte

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.

if total_centro > meta_centro:
    estado_centro = 'meta superada'
elif total_centro == meta_centro:
    estado_centro = 'igualo la meta'
else:
    estado_centro = 'meta no alcanzada'
if total_norte > meta_norte:
    estado_norte = 'meta superada'
elif total_norte == meta_norte:
    estado_norte = 'igualo la meta'
else:
    estado_norte = 'meta no alcanzada'

# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    rango_mayor = 'tienda centro'
elif total_norte > total_centro:
    rango_mayor = 'tienda del norte'
else:
    rango_mayor = 'ambas tiendas tienen el mismo rango'
    
print("          comparacion semanal de tiendas")
print('-'*60)
print(f"   total ventas del centro:    {total_centro:,.2f} ")
print(f"   total ventas del norte:     {total_norte:,.2f} ")
print('-'*60)
print(f'  meta del centro: {meta_centro:,.2f}, | {porcentaje_centro:,.1f}%')
print( f'  {estado_centro}')
print(f'  meta del norte: {meta_norte:,.2f}, | {porcentaje_norte:,.1f}%')
print(f'  {estado_norte}')
print('-'*60)
print(f'  tienda con mayor recaudacion: {rango_mayor}')

# TODO: presenta un reporte con etiquetas claras y f-strings.
# TODO: escribe las tres conclusiones solicitadas en la guía.
