# Se analiza los promedios finales de los 500 egresados del 2024 en La Ligua
# El programa debe calcular e informar:
# - Cantidad de mujeres
# - Promedio de notas de estudiantes varones del listado
# - Cuántos varones tuvieron notas sobre 5.5
# - Nota más baja
# - Posición del número de registro que se encuentra más alto

notas = []

# Se asume que el número de egresados es fijo (500)
egresados = 500
print("promedios finales de los 500 egresados del 2024 en La Ligua")

for i in range(egresados):
    print(f"Estudiante {i + 1}:")
    nombre = input("Ingrese el nombre del estudiante: ")
    sexo = input("Ingrese el sexo del estudiante (M/F): ").upper()
    nota = float(input("Ingrese la nota del estudiante: "))
    registro = int(input("Ingrese el número de registro del estudiante: "))
    
    # Guardar los datos en una lista
    notas.append((nombre, sexo, nota, registro))

# Inicializar variables
cantidad_mujeres = 0
suma_varones = 0
cantidad_varones = 0
notas_sobre_5_5 = 0
nota_mas_baja = float('inf')
registro_mas_alto = -1
posicion_mas_alto = -1

# Procesar los datos
for i, (nombre, sexo, nota, registro) in enumerate(notas):
    if sexo == 'F':
        cantidad_mujeres += 1
    elif sexo == 'M':
        suma_varones += nota
        cantidad_varones += 1
        if nota > 5.5:
            notas_sobre_5_5 += 1
    if nota < nota_mas_baja:
        nota_mas_baja = nota
    if registro > registro_mas_alto:
        registro_mas_alto = registro
        posicion_mas_alto = i + 1  # Ajustar a posición 1-indexada

# Calcular el promedio de notas de varones
promedio_varones = suma_varones / cantidad_varones if cantidad_varones > 0 else 0

# Mostrar resultados
print("\nResultados del análisis:")
print("Cantidad de mujeres:", cantidad_mujeres)
print("Promedio de notas de varones:", promedio_varones)
print("Cantidad de varones con notas sobre 5.5:", notas_sobre_5_5)
print("Nota más baja:", nota_mas_baja)
print("Posición del número de registro más alto:", posicion_mas_alto)