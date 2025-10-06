#creando diccionario con dict()
diccionario = dict(nombre="Larex",apellidos="Taison")
print(diccionario)

#Las listas no pueden ser claves

diccionario = {("Larex","Taison"):"XD"}
diccionario = {frozenset(["Larex","Taison" ]):"XD"} #-----> Solo funciona en conjunto con "frozenset"
#diccionario = {["Larex","Taison"]:"XD"} #----> [] Da error porque es unhashable
print(diccionario)

#Creando diccionarios con fromkeys() valor por defecto: None
diccionario = dict.fromkeys(["nombre","apellido"])

#Creando diccionarios con fromkeys() cambiando el valor por defecto a "NO SE"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")

print(diccionario)
