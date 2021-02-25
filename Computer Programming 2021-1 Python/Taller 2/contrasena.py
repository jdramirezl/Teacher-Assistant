contrasena_guardada = "123admin"

contrasena_ingresada = input("Digite su contraseña ingresada: ")

contrasena_ingresada = contrasena_ingresada.lower()

if contrasena_ingresada == contrasena_guardada:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")