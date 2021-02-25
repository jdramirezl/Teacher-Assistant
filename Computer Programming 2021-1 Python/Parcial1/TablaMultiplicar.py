
'''
Funcion que imprima tabla de numero k de 1 a 10
'''

def tabla():
    k = int(input("Ingrese el numero: "))
    n = 1
    
    for i in range(1, 11):
        print(k*i)

tabla()