edad = int(input("Digite su edad: "))
salario = int(input("Digite su salario: "))

if edad > 16 and salario > 1000000:
    print("Debe tributar")
else:
    print("No debe tributar")