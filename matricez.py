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



# hotel = [['Vacia' for _ in range(6)] for _ in range(10)]


# costo_por_habitacion = 100  # Definir un costo por habitación ocupada


# print("**BIENVENIDO AL HOTEL GARGOLA**")

# def agendar_habitacion():
#     piso = int(input("Ingrese el número de piso (1-10): ")) - 1
#     habitacion = int(input("Ingrese el número de habitación (1-6): ")) - 1

#     if hotel[piso][habitacion] == 'Vacia':
#         nombre = input("Ingrese su nombre: ")
#         hotel[piso][habitacion] = nombre
#         print(f"Habitación agendada exitosamente para {nombre}.")
#     else:
#         print("¡Advertencia! La habitación ya está ocupada.")

# def ver_estado_hotel():
#     print("Estado del hotel:")
#     for i in range(10):
#         print(f"Piso {i+1}: ", end="")
#         for j in range(6):
#             if hotel[i][j] == 'Vacia':
#                 print(f"Habitación {j+1}: Vacía", end="  ")
#             else:
#                 print(f"Habitación {j+1}: {hotel[i][j]}", end="  ")
#         print()

# def verificar_disponibilidad():
#     habitaciones_vacias = 0
#     for i in range(10):
#         for j in range(6):
#             if hotel[i][j] == 'Vacia':
#                 habitaciones_vacias += 1
#     print(f"Habitaciones disponibles: {habitaciones_vacias}")

# def monetizar():
#     total_recaudado = 0
#     for i in range(10):
#         for j in range(6):
#             if hotel[i][j] != 'Vacia':
#                 total_recaudado += costo_por_habitacion
#     print(f"Total recaudado: ${total_recaudado}")

# def menu():
#     while True:
#         print("\n--- Menú ---")
#         print("1. Agendar habitación")
#         print("2. Ver estado del hotel")
#         print("3. Verificar disponibilidad de habitaciones")
#         print("4. Monetizar")
#         print("5. Salir")
        
#         opcion = int(input("Ingrese una opción: "))

#         match opcion:
#             case 1:
#                 agendar_habitacion()
#             case 2:
#                 ver_estado_hotel()
#             case 3:
#                 verificar_disponibilidad()
#             case 4:
#                 monetizar()
#             case 5:
#                 print("Saliendo del sistema...")
#                 break
#             case _:
#                 print("Opción no válida. Por favor intente de nuevo.")

# # Ejecutar el menú
# menu()

# actividad del hotel por profesor

hotel = [
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
]
t=0
def resv(piso, num_habi, nombre):
    if not hotel[piso][num_habi]:  # Verificar si la habitación está vacía
        hotel[piso][num_habi] = nombre
        print(f"Reserva realizada para {nombre} en el piso {piso}, habitación {num_habi}.")
    else:
        print(f"Estimado/a {nombre}, la habitación {num_habi} del piso {piso} se encuentra ocupada, redireccionando a menú principal.")

def guardar_reserva(piso, num_habi, nombre):
    with open("hotel.txt", "w") as archivo:
        archivo.write(f"Su habitacion esta en el piso {piso+1}, numero {num_habi+1}. Gracias por su compra :D, {nombre}.")

def saber(hotel):
    for i, piso in enumerate(hotel):
        for j, habitacion in enumerate(piso):
            if not habitacion:
                print(f"Habitación {j+1} del piso {i+1} está disponible.")
            else:
                print(f"Habitación {j+1} del piso {i+1} está lamentablemente ocupada.")
                
def monetizar(t):
    for i, piso in enumerate(hotel):
        for j, habitacion in enumerate(piso):
            if habitacion:
                if i>=0 and i<=2:
                    t=t+78500
                elif i>=3 and i<=6:
                    t=t+90000
                elif  i>=7 and i<=9:
                    t=t+110000      
    return t

while True:
    print("Bienvenido al hotel duocuc")
    print("""
 // ¿Qué desea hacer? //
1. Reservar una habitación.
2. Ver todas las habitaciones.
3. Verificar disponibilidad de habitaciones.
4. Monetizar
5. Salir.
    """)
    op = int(input("Seleccione una opción: "))
    match op:
        case(1):
            piso = int(input("Ingrese el piso: "))-1
            num_habi = int(input("Ingrese el número de su habitación: "))-1
            nombre = input("Ingrese su nombre para la reserva: ")
            resv(piso, num_habi, nombre)
            guardar_reserva(piso, num_habi, nombre)
        case (2):
            for piso in hotel:
                print(piso)
        case (3):
            saber(hotel)    
        case (4):
            print("El total monetizado es ", (monetizar(t))*1.19)
        case (5):
            print("usted ha salido")
            break
        case (_):
            print("opcion invalida ._.")


#actividad de cine 


# def reservar(matriz):
#     try:
#         asiento=int(input("Ingrese el asiento que desea reservar: "))


#         for i in range (10):
#             for e in range(10):

#                 if asiento == matriz[i][e]:
#                     print("Asiento disponible")
#                     if matriz[i] == 0:
#                         print(f"El precio del asiento {asiento} es {precio1} ")
#                         print(f"El codigo de su asiento es {i},{e}")
#                         asiento2=asiento
#                         matriz[i][e]="XX"
#                         menu()
#                         break
#                     elif matriz[i] == 1:
#                         print(f"El precio del asiento {asiento} es {precio2} ")
#                         print(f"El codigo de su asiento es {i},{e}")
#                         matriz[i][e]="XX"
#                         asiento2=asiento
#                         menu()
#                         break
#                     else:
#                         print(f"El precio del asiento {asiento} es {precio3} ")
#                         print(f"El codigo de su asiento es {i},{e}")
#                         matriz[i][e]="XX"
#                         asiento2=asiento
#                         menu()
#                         break     
#     except:
#         print("Ingrese un asiento valido")

# def buscar(matriz):
#     print("A continuacion debera ingresar el codigo del asiento")
#     num1=int(input("Ingrese el primer numero"))
#     num2=int(input("Ingrese el segundo numero"))
#     for i in range(10):
#         for e in range(10):
#             if matriz[i][e]==matriz[num1][num2]:
#                 print(f"Su asiento es: {matriz[i][e]}")
#                 menu()

# def mostrar(matriz):
#     for fila in range(10):
#         for columna in range(10):
#             if fila == 0 :
#                 print(matriz[fila][columna], end=" ")
#             elif columna == 9:
#                 print(matriz[fila][columna], end="\n")
#             else:
#                 print(matriz[fila][columna], end="\t")
#     menu()



# def menu():
#     print("Bienvenido Al Menu Del Cine")
#     print("1.- Reservar Asiento")
#     print("2.- Buscar Asiento")
#     print("3.- Vizualizar Asientos")
#     print("4.- Visualizar Ventas")
#     print("5.- Guardar Informacion Del Dia")
#     print("6.- Salir")

#     op=int(input("Ingrese ina opcion: "))

#     match op:
#         case 1:
#             reservar(cine)
#         case 2:
            
#             buscar(cine)
#         case 3:
#             mostrar(cine)
#         case 6:
#             breakpoint

# precio1=10000
# precio2=18500
# precio3=21500

# cine=[[1,2,3,4,5,6,7,8,9,10],
#       [11,12,13,14,15,16,17,18,19,20],
#       [21,22,23,24,25,26,27,28,29,30],
#       [31,32,33,34,35,36,37,38,39,40],
#       [41,42,43,44,45,46,47,48,49,50],
#       [51,52,53,54,55,56,57,58,59,60],
#       [61,62,63,64,65,66,67,68,69,70],
#       [71,72,73,74,75,76,77,78,79,80],
#       [81,82,83,84,85,86,87,88,89,90],
#       [91,92,93,94,95,96,97,98,99,100],
#       ]


# menu()



# Sistema de Gestión de Estacionamiento

# Configuración inicial del estacionamiento
filas = 6
espacios_por_fila = 12
estacionamiento = [["Disponible" for _ in range(espacios_por_fila)] for _ in range(filas)]
tarifas = [3000, 3000] + [1500] * 4  # Tarifas para las primeras 2 filas y las restantes
ventas_totales = 0

# Funciones
def mostrar_estado():
    print("\nEstado del estacionamiento:")
    for i, fila in enumerate(estacionamiento):
        print(f"Fila {i+1}: {fila}")

def reservar_estacionamiento():
    global ventas_totales
    fila = int(input("Ingrese el número de fila (1-6): ")) - 1
    espacio = int(input("Ingrese el número de espacio (1-12): ")) - 1
    if 0 <= fila < filas and 0 <= espacio < espacios_por_fila:
        if estacionamiento[fila][espacio] == "Disponible":
            estacionamiento[fila][espacio] = "Reservado"
            ventas_totales += tarifas[fila]
            print("Reserva realizada con éxito.")
        else:
            print("El espacio ya está reservado.")
    else:
        print("Ubicación inválida.")

def anular_reserva():
    fila = int(input("Ingrese el número de fila (1-6): ")) - 1
    espacio = int(input("Ingrese el número de espacio (1-12): ")) - 1
    if 0 <= fila < filas and 0 <= espacio < espacios_por_fila:
        if estacionamiento[fila][espacio] == "Reservado":
            estacionamiento[fila][espacio] = "Disponible"
            print("Reserva anulada con éxito.")
        else:
            print("El espacio no está reservado.")
    else:
        print("Ubicación inválida.")

def totalizar_ventas():
    print(f"Las ventas totales del día son: ${ventas_totales}")

# Menú principal
def menu():
    while True:
        print("\nSistema de Gestión de Estacionamiento")
        print("1. Reservar estacionamiento")
        print("2. Anular reserva")
        print("3. Ver estado del estacionamiento")
        print("4. Totalizar ventas del día")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reservar_estacionamiento()
        elif opcion == "2":
            anular_reserva()
        elif opcion == "3":
            mostrar_estado()
        elif opcion == "4":
            totalizar_ventas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

# Ejecutar el programa
menu()