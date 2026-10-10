"""Microreto: el portero del café."""

energia = int(input("Cuanta energía tienenes de 0-100?: "))
trae_cafe = input("¿Traes café? (si/no): ").lower().strip() == "si"

mensaje = "Completa las reglas del portero."

# TODO: usa and para detectar energía baja sin café.
if energia < 30 and not(trae_cafe): # not(trae_cafe) | Trae_Cafe == False
    mensaje = "Acceso denegado: necesitas dormir o tomar café."
# TODO: usa or para permitir energía suficiente o café.
elif energia >=30 or trae_cafe: #trae_cafe == True
    mensaje = "Acceso permitido: pasa, pero comparte café."
# TODO: escribe mensajes claros para cada resultado.
else:
    mensaje = "El guarda está confundifo, revisa las respuestas."

print(mensaje)
