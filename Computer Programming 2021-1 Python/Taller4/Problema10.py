

def temperatura2(grados, escala, convertir):
    resultado = 0
    
    if escala == "Farenheit":
        if convertir == "Kelvin":
            resultado = ((5*(grados-32))/(9)) + 273.15
        elif convertir == "Celsius":
            resultado = ((9/5)*grados)+32
            
    elif escala == "Kelvin":
        if convertir == "Farenheit":
            resultado = (9*(grados-273.15)/(5))+32
        elif convertir == "Celsius":
            resultado = grados-273.15
            
    elif escala == "Celsius":
        if convertir == "Farenheit":
            resultado = (9/5)*grados+32
        elif convertir == "Kelvin":
            resultado = grados + 273.15
    
    return resultado

print(temperatura2(50, "Farenheit", "Kelvin"))