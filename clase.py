numero = int(input("ingrese un numero: "))
cont = 0  
mult = 0  
sum = 0
while cont<numero:
    print("numero", cont+1)
    if (cont+1)%3 == 0:
        mult+1
        sum = cont+1
    cont = cont + 1
    print(f"hay {mult} multiplos en {numero}")
    print(f"la suma de los multiplos es {sum}")
