
temp = int(input("Digite el temperatura: "))
edad = int(input("Digite su edad: "))

if temp > 27 and edad >= 18:
    dinero = int(input("Digite su dinero: "))
    if dinero > 5:
        print("Comprar helado cerveza")
    else:
        print("Lo sentimos estas pobre")
else:
    print("Lo sentimos juventud")
