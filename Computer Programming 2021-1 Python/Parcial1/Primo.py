num = int(input("Ingrese numero: "))

ndivisores = 0
for divisor in range(1, num+1, 1):
    if num % divisor == 0:
        ndivisores += 1

if ndivisores > 2:
    print("El numero", num, "no es primo")
else:
    print("El numero", num, "es primo")
