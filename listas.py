# #      0,1, 2, 3,4, 5
# lista=[1,76,65,9 "lol" ,7,54]
#                   -3   -2 1-

# print(lista)

# lista.append("mario") para agregar un nombre

# lista.append(3,round(856.897)) para agregar numeros decimales y redondearlos

# lista.remove(76)      para remover o quitar caracteres dentro de la lista

# lista.reverse()       para remover la lista o reversar

# lista.sort()          para ordenar una lista

#lista.count()          para mostrar el total de elementos.

#lista.clear ()         para eliminar todos los elementos de la lista.

#lista.index ()         muestra el indice del elemento que va en el argumento




#lista.insert(3,"mario")


# print(lista)

# runtime ("tiempo de ejecucion")



# for i in lista:
#     print("Elemento ",i)
    
    
# while True:
    
#     print(lista)
    
#     elemento=int(input("agregue un nuevo elemento:  "))
#     lista.append(elemento)
#     print(lista)



#               0         1      2
# lista_nombre=["Pedro", "Juan", "Diego"]

# lista_apellido=["Rosas", "Gonzales,", "Robles"]

# car=["primer","segundo","tercer"]
 
# for i in range(len(lista_nombre)):
#      print("el", car[i], "nombre es:   ", lista_nombre[i],lista_apellido[i])
     
     
#hacer una lista de frutas poner una fruta, eliminar otra y luego mostrar el resultado.

#hacer una lista de nombres(3), usar una lista de frutas (5), crear el p

# listaFruta=["Pera","Manzana","Platano","limon","naranja"]

# print(listaFruta)

# listaFruta.remove("Platano")


# print(listaFruta)


# listaFruta.insert(2,"kiwi")

# print(listaFruta)


     
     
# print("BIENVENIDO AL LOCAL")



# lista_nombre=["Pedro", "Juan", "Diego"]

# listaFruta=["Pera","Manzana","Platano","limon","naranja"]

# contador=1

# carrito=[]

# preciofruta=[900,800,700,1000,600]

# total=0

# print("quien va a comprar?:   ")

# for i in lista_nombre:
#     print(contador,".-",i)
#     contador+=1
    
# sel=int(input())-1

# # print(lista_nombre[sel])

# print("bienvenido", lista_nombre[sel], "a la fruteria")

# while len(carrito)<3:
#     for fruta in range(len(listaFruta)):
#         print(fruta+1, ".-", listaFruta[fruta])
#     selfru=int(input("seleccione una fruta: "))-1
#     print("usted ha seleccionado", listaFruta[selfru]," y su precio es:  ", preciofruta[selfru])
#     carrito.append(selfru)
#     print(carrito)        
# print("Verduderia Pelayos")
# for i in range(len(carrito)):
#     print(f"",{listaFruta[i]},".....", preciofruta[i])
#     total=total+preciofruta[i]
    
# print("su total fue:    ", total, "vuelva pronto...", lista_nombre[sel])


# ----clase del 24 de enero con listas

#pedir un numero y del 1 a ese numero poner en una lista los pares y en otra los impares. printear ambas listas


# num=7
# pares=[]
# impares=[]



# for i in range(num):


#     if (i+1) %2==0:
#         pares.append(i+1)

#         print("el numero es positivo y par")
#     else:
#         impares.append(i+1)
        
# print("Pares=   ", pares)
# print("Impares=   ",impares)

#crear un programa para ingresar notas para dejar de ingresar notas, debe ingresar u cero, finalmente debe mostrar el promedio USAR LISTAS


# def ingresar_notas():
#     notas = []
#     while True:
#         nota = float(input("Ingrese una nota (presione 0 para terminar): "))
#         if nota == 0:
#             break
#         notas.append(nota)
    
#     if notas:
#         promedio = sum(notas) / len(notas)
        
#         print(f"El promedio de las notas es: {promedio:.2f}")
#     else:
#         print("No se ingresaron notas.")

# ingresar_notas()


#pedir a un usuario su nombre completo y mostrar en la parte inferior, sus nombres y apellidos ordenados afabeticaente y mostrar la cantidad de caracteres
#del nombre ingresado



# nom=["axel","brian"]

# apell=["brogi","pinilla"]

# carac=["primer","segundo"]

# print(nom)

# print(apell)

# nom.sort()

# apell.sort()


# for i in range(len(nom)):
#     print("su", carac[i], "nombre es:", len(nom[i]), "y apellido es: ", apell[i])
    




#ingresar patentes a una lista y mostrar al usuario un advertencia si la patente fue ingresada. mostrar el listado de patentes al final de forma inversa de como entraron al parkin


# def main():
#     patentes = []
    
#     while True:
#         patente = input("Ingrese una patente (o 'salir' para terminar): ")
#         if patente.lower() == 'salir':
#             break
#         if patente in patentes:
#             print("Advertencia: La patente ya fue ingresada.")
#         else:
#             patentes.append(patente)
    
#     print("Listado de patentes en orden inverso:")
#     for patente in reversed(patentes):
#         print(patente)

# if __name__ == "__main__":
#     main()


# korn=[]
# marcas=[]
# while korn!="0":
#     korn=input("ingrese la marca deseada:   ")
#     marcas.append(korn)
#     marcas.sort()
#     print(marcas)
    
    
    
#actividad temperatura con listas.


# temp=[23,29,31,32,21,22,34,28]

# print(round(sum(temp)/len(temp)))

# print(temp)


# for i in temp:
#     if i>=28:
#         print(i,"hace mucha calor")
#     else:
#         print(i,"hace calor pero agradable")
        
        
        
# ---------------ACTIVIDAD LOTERIA-----------------

# import random

# # Crear una lista vacía
# loteria = []

# # Generar 7 números aleatorios y añadirlos a la lista
# for _ in range(7):
#     number = random.randint(1,38)  # Puedes ajustar el rango según tus necesidades
#     loteria.append(number)

# # Imprimir la lista de números aleatorios
# print(loteria)



# colo=[]
# u=[]
# op="1"
# while op!="0":
    
#     print("A que equipo desea agregar?, para salir presione cero(0) ")
#     op=input()
#     if op=="colo":
#         numjugador=int(input("ingrese numero del jugador:   "))
#         colo.append(numjugador)
#     else:
#         numjugador=int(input("ingrese numero del jugador:   "))
#         u.append(numjugador)
        
        
#         print(colo)
#         print(u)
        
        
# Pedir al usuario que ingrese 3 nombres clase del 27 de enero

nombres = []
for i in range(3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)

nombre_mayor_longitud = max(nombres, key=len)

print(f"El nombre con mayor cantidad de caracteres es: {nombre_mayor_longitud}")