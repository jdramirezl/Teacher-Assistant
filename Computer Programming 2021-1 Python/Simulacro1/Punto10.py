'''
Cree un programa en Python y dentro 
cree un ciclo while infinito. 
Pídale al usuario dentro del ciclo un número (int) (num). 

Si el usuario ingresa 0, 
detenga el ciclo (utilice un break). 

Si el usuario ingresa cualquier otro número, 
muestre ese número multiplicado por 3. 
'''

while True:
    numero = int(input("Ingrese un numero: "))
    
    if numero == 0:
        break
    else:
        multiplicacion = numero * 3
        print(multiplicacion)
    