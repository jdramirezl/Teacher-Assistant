tipo_de_pizza = input("Pizza vegetariana o no vegetariana: ")

if tipo_de_pizza == "vegetariana":
    print("Ingredientes disponibles: pimiento, tofu")
    ingrediente = input("Que ingrediente quieres: ")
    
elif tipo_de_pizza == "no vegetariana":
    print("Ingredientes disponibles: peperoni, jamon, salmon")
    ingrediente = input("Que ingrediente quieres: ")

print("Pediste una pizza "+tipo_de_pizza+" de ingredientes: Mozarrella, tomate y "+ingrediente)

