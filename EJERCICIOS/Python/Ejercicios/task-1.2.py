# Pedirle al usuario que diga
# cualquier texto real y:

# - Calcular cuanto tardaria en
# decir esa frase

# - Cuantas palabras dijo?

# Si se tarda mas de 1 minuto:

# - Decirle: “para flaco tampoco
# te pedi un testamento”.

# Dalto habla un 30% mas rapido:
# Cuanto tardaria él en decirlo?



# RESOLVIENDO A y B

#le pedimos al usuario que nos diga una frease (o varias)
frase = input("Decime una frase y te calculo cuanto tardarias si tuviera que decirlo: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#Calculamos cuanto tardaria en decir las palabras y se lo decimos. En caso de que tarde le decimos que pare un poco
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras *100 // 2 *1.3 / 100} segundos")
if cantidad_de_palabras > 120:
    print("Para flaco, tampoco te pedi un testamento")