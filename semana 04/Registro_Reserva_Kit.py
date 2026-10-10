# TODO: solicita los datos.
# TODO: limpia los textos.
# TODO: convierte los números con try.
# TODO: valida las entradas.
# TODO: aplica las reglas.
# TODO: muestra el resultado.


nombre = input('por favor, ingrese su nombre: ') .upper() .strip()
kit = input('ingrese el tipo de kit: ').lower() .strip()
try:
    cantidad = int(input('ingrese la cantidad de kits: '))
    if cantidad < 1:
        print('error la cantidad minima es 1')
except ValueError:
    print('cantidad de kits invalido, ingrese del 1 al 100 ')
    cantidad = -1
try:
    dias = int(input('ingrese el numero de dias: '))
    if cantidad < 1:
        print('error la cantidad minima es 1')
except ValueError:
    print('cantidad de dias invalido, ingrese del 1 al 100')
    dias = -1
autorizacion = input('tiene autorizacion (si/no) : ').lower() .strip() == 'si'

if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = "registro rechazado: revise los datos ingresados!"
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f'solicitud aprovada para {nombre}: {cantidad} kits(s) de {kit}'
else:
    resuelto: "solicitud enviada a revision" 
print(resultado) 