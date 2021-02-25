'''
Cree un programa en Python que le pida al usuario por pantalla un número (int) ("n"). 
Luego cree un ciclo que se ejecuta tantas veces como el número "n" recibido anteriormente. 
Luego dentro del ciclo pida al usuario otro número por pantalla. Si el número recibido es par, 
sumelo en un acumulador, si no, no lo sume. Al final, muestra la suma total de los pares. 
'''

n = int(input("Digite el n: "))

acumualador = 0
for i in range(0, n, 1):
    numero = int(input("Digite un numero: "))
    
    if numero%2==0:
        acumualador += numero

print(acumualador)

