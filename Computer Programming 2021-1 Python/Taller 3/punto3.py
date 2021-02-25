n = int(input("Ingrese el valor: "))

total = 0
for numero in range(n+1):
    total += numero**2

print("La suma es: "+ str(total))
