renta = int(input("Digite su renta: "))

if renta < 10000:
    print("Tipo: 5%")
elif 10000 <= renta < 20000:
    print("Tipo: 15%")
elif 20000 <= renta < 35000:
    print("Tipo: 20%")
elif 35000 <= renta < 60000:
    print("Tipo: 30%")
else:
    print("Tipo: 45%")