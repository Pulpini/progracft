# Ejercicio 3: Crear un programa que pida la edad de una persona y diga si es mayor o menor de edad. 
cantidad_personas = int(input("ingrese cantidad de personas: "))
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")