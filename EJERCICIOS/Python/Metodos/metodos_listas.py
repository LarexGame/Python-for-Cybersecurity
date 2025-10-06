#LIST - crea una lista

#LEN - cuenta la cantidad de elementos de una lista

#APPEND - agrega un elemento a la lista
#INSERT - agrega un elemento a la lista en el indice especificado
#EXTEND - agrega varios elementos a la lista

#POP - elimina un elemento de una lista, pide indice y devuelve valor
#REMOVE - remueve un elemento de una lista, pide valor
#CLEAR - elimina todos los elementos de una lista

#SORT - ordena una lista de forma ascendente a descendente
#REVERSE - invierte los elementos de una lista


# CREANDO LISTA CON list()
lista = list(["cadena", 34, "tamaniada"])

# Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista) 

# Agregando un elemento a la lista
lista.append("Traigable")

# Agregando un elemento a la lista en un indice especifico
lista.insert(2, "XD")

# Agregando varias cosas a la lista
lista.extend([True, 2023]) # -> Es importante que se use [] porque se esta agregando una lista

# Eliminando un elemento por su indice
lista.pop(0) # -1 para eliminar el ultimo elemento y asi sucesivamente (-2, -3...)

# Removiendo un elemento de la lista por su valor
lista.remove("XD")

# Eliminando todos los elementos de la lista
# lista.clear -> Elimina la lista

# Ordenando la lista de forma ascendente (Si usamos el parametro reverse=True lo ordena en reverza)
# lista.sort() # -> No funciona si hay texto en la lista (El True y False no se incluyen como texto)

# Invirtiendo los elementos de una lista
lista.reverse()

# Verificando si el elemento esta en la lista
elemento_encontrado = lista.index(34)

print(dir(set(["wakawaka", "miseria"])))


