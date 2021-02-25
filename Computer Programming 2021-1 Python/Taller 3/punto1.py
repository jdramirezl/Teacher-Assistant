
numero_de_llantas = int(input("Ingrese cantidad de llantas: "))
preciounitario = int(input("Ingrese precio unitario: "))

total = numero_de_llantas*preciounitario

if numero_de_llantas > 4:
    total = total - ((10*total)/100)

print("Debe pagar: ", total)



