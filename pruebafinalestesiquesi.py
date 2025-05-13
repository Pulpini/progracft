#caso a analizar: estudiantes de enseñanza media que continuan sus estudios superiores
#se analiza la brecha de genero
#se analiza los promedios finales de los 500 egresados del 2024 en la ligua
#el programa debe calcular e informar catidad de mujeres
#promedio de notas de estudiantes varones del listado
#informar cuantos varones tubieron notas sobre 5,5
#informar nota mas baja
#informar posición del numero de registro que se encuentra mas alto
#describir como lo solucionó
#debe contener while y listas
#utilizar ciclos
encuestados = []
genero = ["femenino, masculino"]
notas = []
while encuestados:
    estudiantes = int(input("Ingrese cantidad de estudiantes encuestados: "))
    notas = int(input("ingrese promedio final del alumno encuestado: "))
    genero = int(input("ingrese el genero del encuestado(femenino/masculino)"))
    encuestados.append({"genero": genero})
    encuestados.append("notas", notas)
#se agregan los datos para ingresarlos a la lista, esto incluye la variable notas, genero y estudiantes
else:
    total_encuestados = len(encuestados)
    total_notas = len(notas)
    genero = [i["femenino"] for i in encuestados]
    promedio = sum(notas) / total_encuestados
    mayor_nota = max(notas)
    minima_nota = min(notas)
    contador_femenino = sum(1 for i in encuestados if i["femenino"] == "femenino") #contador femenino para poder generar resultados
    mayores_masculino = sum(1 for i in encuestados if i["masculino"] > promedio)#se saca el mayor masculino
    posición = notas.index (max(notas))#sacarl el maximo y posicion de las notas
    nota_sobresaliente = notas < 5.5


    print(f"El número total de encuestados es de: {total_encuestados}")
    print(f"El promedio es de: {promedio:.2f}")
    print(f"el mayor promedio mascuino es de : {'mayores_masculino'}")
    print(f"la nota minima es de : {minima_nota}")
    print(f"la nota maxima se coloca en:", posición)
    print(f"las notas sobre 5.5 son:", nota_sobresaliente)
    #resultados de los datos ingresados

   