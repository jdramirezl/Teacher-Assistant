kilometros = int(input("Digite su kilometraje: "))
kilogramos = int(input("Digite su peso de equipaje: "))
medio = input("Digite su medio de transporte: " )

medio = medio.lower()

if medio == "tren":
    valor_total = 2000 + kilometros * 1000.3 + kilogramos * 75
    print("Su valor para tren es: "+str(valor_total))
elif medio == "bus":
    valor_total = 1000 + kilometros * 500.8 + kilogramos * 50
    print("Su valor para bus es: "+str(valor_total))
elif medio == "barco":
    valor_total = 500 + kilometros * 300.5 + kilogramos * 75
    print("Su valor para barco es: "+str(valor_total))