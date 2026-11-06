"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.


# Preparar acumuladores y estructuras
total_minutos = 0

categorias = {
    "Acceso": 0,
    "Equipo": 0,
    "Red": 0
}

pendientes = 0
provincias_pendientes = set()
casos_urgentes = []

caso_mas_largo = ("", 0)

# Recorrer todas las incidencias una sola vez
for caso in incidencias:

    minutos = caso["minutos_atencion"]
    categoria = caso["categoria"]

    # Acumular minutos
    total_minutos += minutos

    # Contar por categoría
    categorias[categoria] += 1

    # Revisar casos pendientes
    if not caso["resuelto"]:

        pendientes += 1

        provincias_pendientes.add(caso["provincia"])

        # Identificar casos urgentes
        if minutos >= 60:
            casos_urgentes.append((caso["id"], minutos))

    # Identificar el caso con más minutos
    if minutos > caso_mas_largo[1]:
        caso_mas_largo = (caso["id"], minutos)

# Calcular promedio
promedio = total_minutos / len(incidencias)

# Mostrar resultados
print("===== REPORTE DE INCIDENCIAS =====")

print("Total de minutos:", total_minutos)
print("Promedio de minutos:", promedio)

print("\nConteo por categoría:")
print("Acceso:", categorias["Acceso"])
print("Equipo:", categorias["Equipo"])
print("Red:", categorias["Red"])

print("\nCasos pendientes:", pendientes)
print("Provincias con pendientes:", provincias_pendientes)

print("\nCasos urgentes:")
print(casos_urgentes)

print("\nCaso con más minutos:")
print(caso_mas_largo)

print("\n¿Hay pendientes en San Jose?")
print("San Jose" in provincias_pendientes)
