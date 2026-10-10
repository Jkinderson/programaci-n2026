"""Microreto: el portero del café."""
#preguntar cuanta energia tiene
#preguntar si trae cafe
# .lower() pone todo en minusculas
# .upper() pone todo en mayusculas
# .strip() quita espacios 
nombre = input('como te llamas?: ').upper().strip()
energia = int(input('cuanta energia tiene del 1 al 100?'))
trae_cafe = input('trae cafe (si/no)?: ').lower().strip() == 'si'


#si vengo con 50% y no tengo cafe = descansar
#si tengo 50% o mas o tengo cafe ingresa a la clase
#cualquier otro escenario = portero confundido

if energia < 50 and not (trae_cafe):
    mensaje = "descansar"
elif energia >= 50 or trae_cafe:
    mensaje = 'ingresa a la clase'
else:
    mensaje = 'portero confundido'
    
print(f'{nombre} -> {mensaje}')