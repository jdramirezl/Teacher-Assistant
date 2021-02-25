nombre = input("Digite su nombre: ")
sexo = input("Digite su sexo: (H - hombre, M - mujer)")


'''
grupo a: (mujer y nombre <- M) (hombre y nombre -> N)
grupo b:
'''
nombre = nombre.upper()
sexo = sexo.upper()

if sexo == "M" and nombre < "M" or sexo == 'H' and nombre > "N":
    print("Pertences al grupo a")
else:
    print("Pertences al grupo b")