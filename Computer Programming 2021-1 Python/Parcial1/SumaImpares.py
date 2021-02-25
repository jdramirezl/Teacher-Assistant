
n = int(input("Ingrese un numero: "))

acumulado = 0
for i in range(1, n + 1, 1):
    if i % 2 != 0:
        acumulado += i

print(acumulado)