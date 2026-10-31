from sedes import sedes

#acceso a lista de sedes de emprendimientos
print("sedes registradas: ", len(sedes))
print("primer sede: ", sedes[0]["nombre"])
print("ventas de la primer sede:", sedes[0]["ventas"])
print("\nANALISIS SEMANAL DE EMPRENDIMIENTOS")
for sede in sedes:
    total = sum(sede["ventas"])
    porcentaje = (total / sede["meta"]) * 100
    
    #clasificacion 
    if porcentaje >= 100:
        clasificacion = "Exitoso"
    elif porcentaje > 80:
        clasificacion = "cerca de la meta"
    else:
        clasificacion = "En riesgo"
    
    print(
        f"{sede['nombre']} | total: {total:,.2f} |"
        f"cumplimiento: {porcentaje:.2f}% | {clasificacion}")