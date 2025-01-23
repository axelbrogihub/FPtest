# #      0,1, 2, 3,4, 5
lista=[1,76,65,9,7,54]
#     -6,-5,-4,-3,-2,-1

print(lista)

# lista.append("mario") para agregar un nombre

# lista.append(3,round(856.897)) para agregar numeros decimales y redondearlos

# lista.remove(76)      para remover o quitar caracteres dentro de la lista

# lista.reverse()       para remover la lista o reversar

# lista.sort()          para ordenar una lista


# lista.insert(3,"mario")


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



listaFruta=["Pera","Manzana","Platano","limon","naranja"]

print(listaFruta)

listaFruta.remove("Platano")


print(listaFruta)


listaFruta.insert(2,"kiwi")

print(listaFruta)


# Lista de nombres
nombres = ["Ana", "Luis", "Carlos"]

# Lista de frutas
frutas = ["Manzana", "Plátano", "Naranja", "Fresa", "Uva"]

# Lista del carrito de compras
carrito = []

# Mostrar nombres disponibles y preguntar quién compra
print("¿Quién va a comprar? Elige un número correspondiente:")
for i, nombre in enumerate(nombres):
    print(f"{i + 1}. {nombre}")

opcion = int(input("Ingresa el número del comprador: "))
comprador = nombres[opcion - 1]
print(f"\n{comprador}, bienvenido a la tienda.\n")

# Mostrar frutas disponibles
print("Estas son las frutas disponibles:")
for i, fruta in enumerate(frutas):
    print(f"{i + 1}. {fruta}")

# Agregar productos al carrito
while True:
    fruta_opcion = int(input("\nSelecciona el número de la fruta que deseas agregar al carrito (0 para terminar): "))
    if fruta_opcion == 0:
        break
    elif 1 <= fruta_opcion <= len(frutas):
        carrito.append(frutas[fruta_opcion - 1])
        print(f"{frutas[fruta_opcion - 1]} se agregó al carrito.")
    else:
        print("Opción no válida, intenta de nuevo.")

# Mostrar boleta
print("\n******** BOLETA DE COMPRAS ********")
print(f"Comprador: {comprador}")
print("Productos en el carrito:")
for i, producto in enumerate(carrito, start=1):
    print(f"{i}. {producto}")
print(f"Total de productos: {len(carrito)}")
print("***********************************")

     
     

         

