n1 = float(input("Digite su n1: "))
n2 = float(input("Digite su n2: "))
n3 = float(input("Digite su n3: "))

total = 0

if n1 <= n2 <= n3: 
    total = n2 + n3
elif  n2 <= n1  <= n3: 
    total = n1 + n3
elif  n3 <= n2 <= n1: 
    total = n1 + n2

print("Total: "+total)
