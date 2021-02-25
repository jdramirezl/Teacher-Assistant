import random

for i in range(10):
    numero_estrellitas = random.randint(1,20) 
    
    print(numero_estrellitas,end=" ")
    for j in range(numero_estrellitas):
        print("*", end="")
    print()
