# 1. Almacenar los datos en una lista
# 2. Mostrar la lista generada
# 3. Contar cuantas asignaturas tiene nota 4.5
# 4. Mostrar las notas de las asignaturas que tiene mayor que 5.0
# 5. Mostrar promedio del alumno
# 6. Muestre la lista ordenada. Detecte la diferencia entre sort y sorted
# 7. Muestre la lista al revés
# 8. Muestre la mejor nota ingresada
# 9. Muestre la peor nota ingresada
# 10. Elimine una nota que usted elija de la lista (de las notas que ingresó inicialmente en su lista)
notas = [6.7, 6.8, 7.0, 4.5, 5.3, 2.0]
asignatura = []
for i in range(6): 
    nota = float(input(f"Ingrese nota asignatura {i + 1}: "))
    asignatura.append(nota)
print("Lista de notas:", asignatura)
print("Cantidad de asignaturas con nota 4.5:", asignatura.count(4.5))
print("Notas mayores a 5.0:", [nota for nota in asignatura if nota > 5.0]) 
print("Promedio del alumno:", sum(asignatura) / len(asignatura))
print("Lista ordenada:", sorted(asignatura)) # sorted devuelve una nueva lista ordenada
print("Lista ordenada (in-place):", asignatura.sort()) # sort ordena la lista en su lugar
print("Lista al revés:", asignatura[::-1]) # Reversa la lista
print("Mejor nota ingresada:", max(asignatura))
print("Peor nota ingresada:", min(asignatura))  
print("Ingrese la nota a eliminar:")
nota_eliminar = float(input())
if nota_eliminar in asignatura:
    asignatura.remove(nota_eliminar)
    print("Lista después de eliminar la nota:", asignatura)
