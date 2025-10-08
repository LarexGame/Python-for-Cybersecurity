#Creando un conjunto con set()
conjunto = set(["dato1", "dato2"])

#Metiendo un conjunto dentro de otro
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}

print(conjunto2)

#Teoria de conjunto

conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

#Verificando si es un subconjunto
resultado = conjunto3.issubset(conjunto4)
resultado = conjunto4 <= conjunto3
print(resultado)

#Verificando si es un superconjunto
resultado = conjunto4.issuperset(conjunto3)
resultado = conjunto3 > conjunto4
print(resultado)

#Verificar si hay algun numero en comun
resultado = conjunto4.isdisjoint(conjunto3)
print(resultado)