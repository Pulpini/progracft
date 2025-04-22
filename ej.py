#escribir un programa que pida login.
#que se pueda solo hasta 3 intentos.
#si falla debe indicar clave bloqueada
correct_login = "martin"
correct_clave = 1234
intentos = 0

while intentos < 3:
    try:
        login = input("Ingrese su login: ") 
        clave = int(input("Ingrese su clave: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        continue
    if login == correct_login and clave == correct_clave:
        print("Bienvenido")
        break
    else:
        print("Login o clave incorrectos")
        intentos += 1
if intentos == 3:
    print("clave bloqueada")
