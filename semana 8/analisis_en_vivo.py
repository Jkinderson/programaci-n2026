"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")

equivalencias = {
    "acetaminofen" : "acetaminofén",
    "paracetamol": "acetaminofén",
    "antiacido": "antíacido",
    "losartán": "losartan"
}

# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
conteo_medicamentos = {}
total_medicamentos = 0
print('\n analisis de fase #1 muestra 3')
for indice in range(3):
    registro = registros[indice]
    print('-'*40)
    print('Información del paciente:')
    print(registro['paciente_nombre'])
    print(registro['paciente_id'])
    print('-'*40)
    print('Información de la atención:')
    print('diagnostico:')
    print(registro['diagnostico'])
    print('medicamentos a tomar:')
    print(registro['medicamentos'])

    for medicamento in registro['medicamentos']:
        #Limpieza PARACETAMOL -> paracetamol -> aceteminofén
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]
        #Contar medicamentos
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1

print('total de medicamentos recetados: ', total_medicamentos)
print(conteo_medicamentos)
# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
print("\nANALISIS FASE #2 MEDICAMENTOS Y ATENCIONES")
conteo_medicamentos = {}
total_medicamentos = 0
conteo_hospital = {}
total_paciente = 0
for registro in registros:
    
    
    for medicamento in registro['medicamentos']:
        #Limpieza PARACETAMOL -> paracetamol -> aceteminofén
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]
        #Contar medicamentos
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
            
print("\nTotal de medicamentos recetados:", total_medicamentos)
for medicamento, cantidad in conteo_medicamentos.items():
    print(f"- {medicamento}:\t {cantidad}")
print("\nTotal de PACIENTES:", total_paciente)
# FASE 3: CONTAR ATENCIONES POR HOSPITAL
conteo_hospital = {}
total_pacientes = 0
for registro in registros:
    total_paciente += 1
    hospital = registro["hospital"]
    if hospital not in conteo_hospital:
        conteo_hospital[hospital] = 0
    conteo_hospital[hospital] +=1
print("\nTotal de PACIENTES:", total_paciente)
for hospital, cantidad in conteo_hospital.items():
    print(f"- {hospital}:\t {cantidad}")
# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA
conteo_enfermedades = {}
for registro in registros:
    enfermedad = registro["diagnostico"]
    if enfermedad not in conteo_enfermedades:
        conteo_enfermedades[enfermedad] = 0
    conteo_enfermedades[enfermedad] += 1
print("\nTotal de ENFERMEDADES DIAGNOSTICADAS:", len(conteo_enfermedades))

