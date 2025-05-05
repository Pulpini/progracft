#crear un programa que solicite numero de boletas a ingresar por usuario.
#se debe solicitar el monto de cada boleta.
#se debe mostrar la suma total de las boletas.
#debe dar el el monto con el iva.
#debe dar tambien cuanto es el monto que ingresa 
boleta = []
iva = 0.19

for i in range(5):
    valor_boleta = int(input(f"Ingrese valor de boleta{i+1}: "))
    boleta.append(valor_boleta)
boleta_con_iva = sum(boleta) * (1 + iva)
ingreso = sum(boleta) / (1 + iva)
print("Lista de boletas:", boleta) 
print("Cantidad de boletas:", len(boleta))
print("Monto de cada boleta:", boleta)
print("Monto total de las boletas:", sum(boleta))#se suma valor de todas las boletas
print("Monto total de las boletas con IVA:", boleta_con_iva)#se multiplica el valor boleta por el iva
print("el monto ingresado al negocio es de:", ingreso)