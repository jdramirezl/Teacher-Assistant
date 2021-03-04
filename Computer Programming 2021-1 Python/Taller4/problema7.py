
def descomponer(numero):
    unidades = numero%10
    decenas = numero//10
    return unidades, decenas

unidades, decenas = descomponer(12)

print(unidades)
print(decenas)



