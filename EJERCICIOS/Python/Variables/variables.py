#####################
# VARIABLES COMUNES #
#####################

a = 2
b = 4
c = a + b

print (c)

nombre = 'Lucas Dalto'
print (nombre)

nombre2 = 40 + 20
print (nombre2)

# Las Variables se declaran y despues se definen y se pueden modificar #

numero = 10
print(numero)

numero2 = 10
numero2 += 2
print(numero2)

numero3 = 10
numero3 -=5
print(numero3)

numero3 = 10
numero3 -=5
numero3 +=3
print(numero3)

# CONCATENAR CON +

nombre3 = 'Lucas'
bienvenida = 'Hola ' + nombre3 + ', Como estas?'
print(bienvenida)

# CONCATENAR CON f-strings

nombre4 = 'Mario'
bienvenida2 = f'Hola {nombre4}, como estas?' # F STRING COLOCA CUALQUIER COSA PUESTO EN LA VARIABLE DETERMINADA
print(bienvenida2)

nombre5 = 'Jorge'
bienvenida3 = f'Hola {nombre5}, Como estas?'
#del bienvenida3 # DEL es comando para eliminar una variable e influye en que orden lo coloques
print(bienvenida3)

nombre6 = 'Rico'
bienvenida4 = f'Hola {nombre6}, Como estas?'
del nombre6 # En este caso, el NOMBRE6 ya fue ejecutado, entonces el DEL no lo puede eliminar antes de ser ejecutado
print(bienvenida4)

# OPERADORES DE PERTENENCIA (in / not in)#

print("Hola" not in bienvenida) 
print("Lucas" in bienvenida2)

# DEFINIENDO UNA VARIABLE CON CAMELCASE

nombreCompletoDeTuTioMaster = 'Lucas'

# DEFINIENDO UNA VARIABLE CON snake_case

nombre_completo_de_tu_tio_master = "Lucas el Master"