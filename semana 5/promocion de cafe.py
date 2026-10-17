producto = ["Cafe", 5000, 20]

porcentaje_aumento = 20

porcentaje_descuento = producto[1] * 15 / 100

ingreso_actual = producto[1] * producto[2]

aumento_unidades = producto[2] + ( producto[2] * porcentaje_aumento / 100)

ingreso_proyectado = ingreso_actual - (porcentaje_descuento * aumento_unidades)

diferencia = ingreso_actual - ingreso_proyectado

if ingreso_proyectado > 0:
    beneficio = "Lanzar"
else:
    beneficio = "No Lanzar"
print ("            Analisis Promocion")
print ("-"*60)
print (f"producto: {producto[0]}")
print (f"Precio Actual: {producto[1]}")
print (f"Unidades Actuales: {producto[2]}")
print (f"Descuento: {porcentaje_descuento} ")
print (f"Precio Promocional: {ingreso_proyectado}")
print (f"Aumento esperado en ventas: {aumento_unidades}%")
print (f"Unidades Proyectadas: {aumento_unidades}")
print (f"Ingreso con promocion: {ingreso_proyectado}")
print (f"Diferencia: {diferencia}")

print (f"Recomendacion: {beneficio}")