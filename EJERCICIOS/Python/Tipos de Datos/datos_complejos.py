# LISTANDO DATOS
# EN PROGRAMACION SE ENUMERA DE 0 A 9

lista = ["LarexGame", "Soy LarexGame", True, 1.76]
print(lista)

lista2 = ["LarexGame", "Soy LarexGame", True, 1.76]
print(lista2[1])

lista2[2] = 'Codigos'

# TUPLAS

tupla = ("LarexGame", "Soy LarexGame", True, 1.76)
print(tupla) # Las TUPLAS no se pueden modificar

#tupla[3] = "Codigo" -> Esto no se puede ejecutar

# CREANDO UN CONJUNTO (set)

conjunto = {"LarexGame", "Soy LarexGame", True, 1.76} #Se puede redefinir, pero no modificar
#print(conjunto[1]) -> El conjunto no puede mostrar valores
# En los conjuntos, no se almacena los datos duplicados

# CREANDO DICCIONARIO (dict)

diccionario = {
    "nombre" : "Larex",
    "Canal" : "LarexGame",
    "esta_emocionado" : True,
    "altura" : 1.76,
    "dato_dupicado" : "Soy Larex"
}

print(diccionario["nombre"]) # DICCIONARIO esta hecho para enumerar vareables/datos

# diccionario = {
    # key : value, -> La coma es importante al finalizar, mientras que la definicion final no lleva ","
#}
