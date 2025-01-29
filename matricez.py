# *****CLASE DEL 27 DE ENERO EMPEZANDO CON MATRICES Y LISTAS*****

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

# #tuplas

# mi_tupla=(1,"dos",3.0)

#diccionario

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

# nombres={"axel":"brogi","gonzalo":"martinez","alvaro":"salas"}

# for key, valor in nombres.items():
#     print(f"{key} {valor}")


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

fut=" Algo mas de texto por aca"

lista=["Mario", "Luigui", "Peach", "TOAD"]

with open('mi_archivo.txt', 'a') as archivo:
    for i in lista:
        archivo.write(f"{i}\n")
    
    
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


#boleta en archivo .txt
