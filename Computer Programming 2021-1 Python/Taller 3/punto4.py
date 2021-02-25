n = int(input("Cantidad de datos: "))

acumulado = 0
for i in range(n):
    numero = float(input("Ingrese el dato "+str(i+1)+": "))
    acumulado += numero

print("El promedio es: " + str(acumulado/n) )

'''
promedio = (suma de datos)/numero datos
'''