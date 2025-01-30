# *****CLASE DEL 27 DE ENERO EMPEZANDO CON MATRICES, LISTAS Y DICCIONARIOS*****

#matriz es una lista compuesta por lista

#       0         1          2

#     0,1,3    0,1,2,3     0,1,2
# m=[[2,7,5], [3,4,7,15], [9,1,2]]




#matriz de 3 dimensiones (3D)

# m=[
#    [
#    [2,7,5],  
#    [3,4,7,15]
   
#    ],
   
#    [
#     [9,1,2],
#     [8,6,71]
#    ]
# ]
# print(m[1][1][0])

# # for i in m:
# #     print(i)

# TUPLAS

# mi_tupla=(1,"dos",3.0)

#**EMPEZANDO CON DICCIONARIOS**

# D={"NOMBRE": "Link", "fonos":
# [
# 988778882,
# 988877776,
# 974512345],
# "activo": True}

# print(D["NOMBRE"])

# for j in D:
#     print(j)


# producto={"uva": 1400, 
#           "pera":1200,
#           "melon":1000,
#           "verduras":{"papa $":600,"lechuga $":700}
#           }

# print(producto)

# for clave, valor in producto.items():
#     print(f"{clave}=${valor}")


# **ACTIVIDAD EN CLASE**

# CASO 1

# Pedir al usuario que ingrese 3 nombres clase del 27 de enero

# nombres = []
# for i in range(3):
#     nombre = input(f"Ingrese el nombre {i+1}: ")
#     nombres.append(nombre)


# nombre_mayor_longitud = max(nombres, key=len)

# print(f"El nombre con mayor cantidad de caracteres es: {nombre_mayor_longitud}")


# CASO 2

# version lista

# lista_nom=["axel","gonzalo","alvaro"]
# lista_apell=["brogi","martinez","salas"]


# car=["primer","segundo","tercer"]

# for i in range(len(lista_nom)):
#     print("el",car[i],"nombres es", lista_nom[i],lista_apell[i])
    
    
# diccionario version

# nombres={"Axel":"Brogi","Gonzalo":"Martinez","Alvaro":"Salas"}
# for key, valor in nombres.items():
#  print(f"SU NOMBRE ES: {key} Y SU APELLIDO ES: {valor}")


# CASO 3


# nombres=[]

# while True:
#     pregunta=input("desea agregar algun nombre?, ingrese (si/no)   ")
#     if pregunta=="no":
#         print("no se agregara otro nombre...")
#         break
#     elif pregunta=="si":
#         print("el programa agregara otro nombre..")
#         nombre=input("ingrese un nombre:    ")
#         nombres.append(nombre)
#     else:
#         print("****ERROR NO VALIDO, PORFAVOR INGRESE OTRO VALOR*****")   
                    
# nombre_menor_longitud = min(nombres, key=len)
# nombres.remove(nombre_menor_longitud)
        
# print(f"el nombre con la menor cantidad de caracteres es: {nombre_menor_longitud}, este nombre sera eliminado")




### clase del 28 de enero archivos txt.

# fut=" Algo mas de texto por aca"

# lista=["Mario", "Luigui", "Peach", "TOAD"]

# with open('mi_archivo.txt', 'a') as archivo:
#     for i in lista:
#         archivo.write(f"{i}\n")
    
    
# archivo = open('mi_archivo.txt', 'r')
# contenido = archivo.read()
# print(contenido)
# archivo.close()

# with open('mi_archivo.txt', 'a') as archivo:
#     for elemento in mi_lista:
#         archivo.write(elemento + '\n')


# import json
# # Datos JSON
# datos = {
# "nombre": "Esteban",
# "edad": 25,
# "comuna": "Santiago",
# "estudios": ["colegio Arturo Prat", "liceo el bosque",
# "Duoc UC", "Diplomado Duoc UC"]
# }
# # Abre el archivo, w es escritura
# with open('archivo.json', 'w') as archivo:
#     json.dump(datos, archivo)
    
    



    
# personas = {}



# while True:

#   nomb = input("Ingrese su nombre: ")

#   eda = int(input("Ingrese su edad: "))

#   personas[nomb] = eda

  

#   salir = input("Para salir presione 'x', para continuar presione enter ")

#   if salir == "x":

#     break

#   else:

#     print("Siga ingresando nombres y edades.")

    

# print("Lista de personas ingresadas:")

# for nombre, edad in personas.items():

#   print(f"Nombre: {nombre}, Edad: {edad} años")
  
# print(personas)


#*****BOLETA EN ARCHIVO TXT*****

# carrito=[]
# f=["uva", "pera", "platano"]
# pf=[1200, 1000, 1300]
# t=0
# while True:
    
#     print("""
#           1.- Comprar
#           2.- Pagar
#           3.- Salir
#           """)
#     op=int(input("Seleccione una opcion"))
#     match op:
#         case 1:
            
            
#             for i in range(len(f)):
#                 print(i+1,".-",f[i] , "=$",pf[i] )
#             sel=int(input("Selecciones los productos a comprar"))
#             carrito.append(sel-1)
#             print(carrito)   
#         case 2:
#             print
#             print()
#             with open('boleta.txt', 'w') as archivo:
#                 archivo.write("Verdureria Guaton de la fruta\n")
#                 archivo.write("-----------------------------\n")
#                 for i in carrito:
#                     archivo.write(f"{f[i]}***${pf[i]}\n")
#                 archivo.write("-----------------------------\n")
#                 for i in carrito:
#                     t=t+pf[i]
#                 t_iva=t*0.19
#                 tt=t+t_iva
#                 archivo.write(f"TOTAL {t}\n")
#                 archivo.write(f"TOTAL IVA {t_iva}\n")
#                 archivo.write(f"TOTAL a PAGAR {tt}\n")
#                 archivo.write("Gracias por su compra\n")
#             print("*****IMPRIMIENDO BOLETA****")
            
                
            
#         case 3:
#             break
#         case _:
#             print("Eleccion no valida, seleccione de 1-3")
            
            
            
#ACTIVIDAD HOTEL CLASE DEL 29 DE ENERO

# El hotel tiene 10 pisos y 6 habitaciones por piso debe tener un menu de
# 1.- agendar habitacion
# 2.- ver estado hotel
# 3.- verificar la disponibilidad de habitaciones
# 4.- monetizar
# 5.- salir


# debe verificar si la habitacion esta vacia , antes de agendar. si no esta vacia, debe mostrar adbertencia cuando se ve el estado del hotel, 
# se debe mostrar habitaciones vacias y las que ya esta agendadas con el nombre de la persona en cuestion.


hotel=[[],[],[],[],[],[]],
[[1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6],
[1,2,3,4,5,6]
]
hotel = [['Vacia' for _ in range(6)] for _ in range(10)]

costo_por_habitacion = 100  # Definir un costo por habitación ocupada


print("**BIENVENIDO AL HOTEL GARGOLA**")

def agendar_habitacion():
    piso = int(input("Ingrese el número de piso (1-10): ")) - 1
    habitacion = int(input("Ingrese el número de habitación (1-6): ")) - 1

    if hotel[piso][habitacion] == 'Vacia':
        nombre = input("Ingrese su nombre: ")
        hotel[piso][habitacion] = nombre
        print(f"Habitación agendada exitosamente para {nombre}.")
    else:
        print("¡Advertencia! La habitación ya está ocupada.")

def ver_estado_hotel():
    print("Estado del hotel:")
    for i in range(10):
        print(f"Piso {i+1}: ", end="")
        for j in range(6):
            if hotel[i][j] == 'Vacia':
                print(f"Habitación {j+1}: Vacía", end="  ")
            else:
                print(f"Habitación {j+1}: {hotel[i][j]}", end="  ")
        print()

def verificar_disponibilidad():
    habitaciones_vacias = 0
    for i in range(10):
        for j in range(6):
            if hotel[i][j] == 'Vacia':
                habitaciones_vacias += 1
    print(f"Habitaciones disponibles: {habitaciones_vacias}")

def monetizar():
    total_recaudado = 0
    for i in range(10):
        for j in range(6):
            if hotel[i][j] != 'Vacia':
                total_recaudado += costo_por_habitacion
    print(f"Total recaudado: ${total_recaudado}")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agendar habitación")
        print("2. Ver estado del hotel")
        print("3. Verificar disponibilidad de habitaciones")
        print("4. Monetizar")
        print("5. Salir")
        
        opcion = int(input("Ingrese una opción: "))

        match opcion:
            case 1:
                agendar_habitacion()
            case 2:
                ver_estado_hotel()
            case 3:
                verificar_disponibilidad()
            case 4:
                monetizar()
            case 5:
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida. Por favor intente de nuevo.")

# Ejecutar el menú
menu()
