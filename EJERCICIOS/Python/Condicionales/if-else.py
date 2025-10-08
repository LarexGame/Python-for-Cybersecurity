# CONDICIONALES DE PYTHON

#if True:
    # accion se ejecuta
    
#if False:
    #accion no se ejecuta
    
edad = 30

if edad >= 18:
    print("Puedes pasar, Makina")

else:
    print("Cagaste compa")
     
usuario_de_base_de_datos = "LarexGame"
usuario_de_escritorio = "LarexGame"
contraseña_almacenada = "Malteada"
contraseña_escrita = "Tragamundos"

if usuario_de_base_de_datos == usuario_de_escritorio:
    print("Iniciando Sesion")
else:
    print("Sos un mongolo")

# IF anidados y ELSE IF (elif)

ingreso_mensual = 100000
gasto_mensual = 95000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:      # El "if" esta dentro de otro, haciendo que tengan condiciones las condiciones
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien pa")
    else:
        print("Deja de gastar, Forro")
elif ingreso_mensual > 1000:   # "elif" es usado para determinar una condicion extra si va a determinar 3 o mas condiciones en una programacion
    print("Estas bien economicamente en LATAM")
else:       # "else" se usa en la ultima condicion que vayas a poner en el codigo
    print("No me hables con ese tono... De piel")