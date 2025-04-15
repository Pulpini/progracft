
#codigo de la prueba del lunes 7 abril
print("bienvenido a calculo de tarifa telefonica CFT")
min_dia = int(input("Porfavor ingrese cantidad de min hablados en horario dia:"))
min_noche = int(input("Porfavor ingrese cantidad de min hablado en horario noche"))
#se consulta por datos necesarios de dia y noche
Calculo_dia = int(min_dia*10)
caluculo_noche = int(min_noche*8)
Calculo_dia_sobrepasado = int(min_dia*15)
caluculo_noche_sobrepasado = int(min_noche*13)
calculo_total = int(Calculo_dia+caluculo_noche)
calculo_total_sobrepasado = int(Calculo_dia_sobrepasado+caluculo_noche_sobrepasado)
#se calcula dia y noche. ademas se realiza aviso cuando se esta sobrepasado 
if min_dia <= 100 and min_noche <= 80:
    print("no excede la tarifa base(100 día y 80 noche)")
if min_dia > 100 and min_noche > 80:
    print("Se excede la tarifa base(100 día y 80 noche)")
print(("Su monto a pagar es de: $"),calculo_total)
print(("En caso de estar sobrepasado debera pagar: $"),calculo_total_sobrepasado)
#debe calcular el total y el total excedido
print("gracias por usar nuestro servicio")
#NO LO MUESTRA !!!!!!!