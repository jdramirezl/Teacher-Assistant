'''
Con una funcion hacer un promedio
Recibimos un numero y tomamos 
todos los menores a este que sean pares
con estos hacer el promedio
'''

def promedio():
    numero = int(input("Digite su numero: "))
    
    acumulado = 0
    pares = 0
    for num in range(1, numero + 1, 1):
        if num%2==0:
            acumulado += num
            pares += 1

    promedio = acumulado/pares
    print(promedio)

promedio()
