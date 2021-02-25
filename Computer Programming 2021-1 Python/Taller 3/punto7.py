import random

#generacion aleotaria
numero_para_adivinar = random.randint(1, 10) 
print(numero_para_adivinar)

intentos = 0
#intentos del usuario
while True:
    adivinado = int(input("Cual numero crees que es: ")) 
    intentos = intentos + 1
    
    if adivinado == numero_para_adivinar:
        print("Ganaste")
        print("Intentos: ",intentos)
        break
    elif adivinado < numero_para_adivinar:
        print("Casi pero no, el numero es mas grande")
    elif adivinado > numero_para_adivinar:
        print("Casi pero no, el numero es mas pequeño")



