# #      0,1, 2, 3,4, 5
# lista=[1,76,65,9,7,54]
#     -6,-5,-4,-3,-2,-1

# print(lista)

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

#hacer una lista de nombres(3), usar una lista de frutas (5), crear el p

# listaFruta=["Pera","Manzana","Platano","limon","naranja"]

# print(listaFruta)

# listaFruta.remove("Platano")


# print(listaFruta)


# listaFruta.insert(2,"kiwi")

# print(listaFruta)


     
     
print("BIENVENIDO AL LOCAL")



lista_nombre=["Pedro", "Juan", "Diego"]

listaFruta=["Pera","Manzana","Platano","limon","naranja"]

contador=1

carrito=[]

preciofruta=[900,800,700,1000,600]

total=0

print("quien va a comprar?:   ")

for i in lista_nombre:
    print(contador,".-",i)
    contador+=1
    
sel=int(input())-1

# print(lista_nombre[sel])

print("bienvenido", lista_nombre[sel], "a la fruteria")

while len(carrito)<3:
    for fruta in range(len(listaFruta)):
        print(fruta+1, ".-", listaFruta[fruta])
    selfru=int(input("seleccione una fruta: "))-1
    print("usted ha seleccionado", listaFruta[selfru]," y su precio es:  ", preciofruta[selfru])
    carrito.append(selfru)
    print(carrito)        
print("Verduderia Pelayos")
for i in range(len(carrito)):
    print(f"",{listaFruta[i]},".....", preciofruta[i])
    total=total+preciofruta[i]
    
print("su total fue:    ", total, "vuelva pronto...", lista_nombre[sel])
    
    





         

