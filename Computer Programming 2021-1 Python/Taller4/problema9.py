
def temperatura(celsius):
    resultado = 0
    if 100 >= celsius >= 0 and celsius%10==0:
        print("Entramos a Farenheit")
        resultado = (9/5)*celsius+32
    else:
        print("Entramos a Kelvin")
        resultado = celsius + 273.15
    
    return resultado

print(temperatura(50))