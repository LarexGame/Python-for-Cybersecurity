# METODOS EN CADENAS

# DIR - Devuelve la lista de atributos validos del objeto pasado

# UPPER - Convierte a Mayuscula
# LOWER - Convierte a Minuscula
# CAPITALIZE - Primera en Mayuscula

# FIND - método encuentra la primera aparición del valor especificado, sino devuelve -1
# INDEX - método encuentra la primera aparición del valor especificado, sino devuelve una excepcion

# ISNUMERIC - si es numerico devuelve true
# ISALPHA - si es alfa numèrico devuelve true

# COUNT - devuelve el número de ocurrencias de una subcadena en la cadena dada.
# LEN - cuenta los caracteres de una cadena

# ENDSWITH- verifica si una cadena comienza con
# STARTSWITH- verifica si una cadena termina con

# REPLACE- remplaza un valor por otro
# SPLIT - separa por el parametro dado



cadena1 = "Hola, soy Larex"
cadena2 = "Bienvenido al mundo del bellaqueo"

resultado = dir(cadena1) # Esto no es un metodo, es una FUNCION DE PYTHON (DIR)

mayus = cadena1.upper() # -> Esto convierte a Mayuscula
minus = cadena1.lower() # -> Esto convierte a Minuscula
primera_letra_mayus = cadena1.capitalize() # -> Esto convierte todo a Minus y coloca la primera letra en Mayus

# BUSQUEDA

busqueda_find = cadena1.find("Hola") # El resultado sera la posicion que se encuentre lo que busques, mas si no encuentra el resultado sera -1

    # CADENA DENTRO CADENA
busqueda_index = cadena1.index("L") # Igual a (find) pero si no encuentra lanza una excepcion

# NUMERICOS DE TRUE OR FALSE

es_numerico = cadena1.isnumeric() # -> Si el texto es numerico, tira True, si no, tira False
es_alfanumerico = cadena1.isalpha() # -> Da true si el texto no tiene caracteres especiales (Los Espacios tambien cuentan)

# BUSQUEDA DE CADENA EN OTEA CADENA

contar_coincidencias = cadena1.count('a') # -> El resultado sera cuantas letras hay en el texto dado. Si no hay, resultado = 0

# CONTAR CARACTERES

contar_caracteres = len(cadena1) # -> LEN es una funcion que cuenta los caracteres de una cadena

# VERIFICACION DE CADENA (TRUE/FALSE)

empieza_con = cadena1.startswith("Hola") # ->Verifica el inicio de una cadena
termina_con = cadena1.endswith("Larex") # -> Verifica el final de la cadena

# REEMPLAZA VALORES

cadena_nueva = cadena1.replace("la","Holu maquina") # -> (X , Y) Si encuentra coincidencia, reemplaza por Y

# SEPARAR CADENAS

cadena_separada = cadena1.split(",") # -> Separa una cadena y la vuelve lista