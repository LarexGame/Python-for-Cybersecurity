# Keys() -> devuelve las claves (Tambien sirve para iterar)

# get() -> devuelve el valor de una clave
# clear() -> elimina todos los elementos
# pop() -> elimina un elemento

# items() -> para iterar el dict

diccionario = {
    "nombre" : "Larex",
    "Canal" : "LarexGame",
    "esta_emocionado" : True,
    "altura" : 1.76,
    "dato_dupicado" : "Soy Larex"
}

claves = diccionario.keys() # -> Nos devuelve un objeto dict_item
nombrar = diccionario.get("Canal") # -> Si no encuentra nada, el programa continua
print(claves)
print(nombrar)

# Eliminando un elemento de el diccionario
diccionario.pop("Canal") # -> Elemento con (_) el programa tira error

# Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

# Eliminando todo el diccionario
diccionario.clear()
