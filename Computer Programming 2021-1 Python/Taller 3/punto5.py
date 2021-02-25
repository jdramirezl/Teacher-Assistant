import random

numero_de_tiradas = int(input("Digite cuantas tiradas de dado: "))

cuantas_veces_tres = 0

for i in range(numero_de_tiradas):
    cara_aleatoria = random.randint(1,7)
    
    if cara_aleatoria == 3:
        cuantas_veces_tres += 1


print("Dio 3: ",cuantas_veces_tres)
