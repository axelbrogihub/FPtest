# nombre="Axel BROGI"
# edad=23

# print("Mi nombre es", nombre, "y mi edad es ", edad)




# print("ingrese un numero")
# num1=int(input())

# print("ingrese otro un numero")
# num2=int(input())



# print(num1+(5*num2+8))



# print("ingrese un numero")
# num1=int(input())

# if num1>0:
#     print("el numero ingresado es positivo")
# else:
#     print("el numero ingresado es negativo o cero")


# print("ingrese su edad")
# num1=int(input())

# if num1>18:
#     print("es mayor de edad")
# else:
#     print("no es mayor de edad")
    
    
# num1=0
# num2=0
# num3=0


# print("ingrese el primer numero")
# num1=int(input())


# print("ingrese el segundo numero")
# num2=int(input())


# print("ingrese el tercer numero numero")
# num3=int(input())


# print((num1+num2+num3)/3)



# un parque nacional que tiene los siguientes valores

# edad=0
# entradas=0

# # menor de 12 $500
# # entre 13 y 18 $1000
# # entre 19 y 64 $2000
# # mas de 65 $700

# print(f"bienvenido al parque nacional")

# print("cual es su edad?")

# edad=int(input())

# if edad<12:
#     print("su entrada cuesta 500 pesos")
#     precio=500
# elif edad>=13 and edad<=18:
#     print("debe pagar 1000 pesos")
#     precio=1000
# elif edad>=19 and edad<=64:
#     print("ud debera pagar 2000 pesos")
#     precio=2000
# elif edad>65:
#     print("debera pagar 700 pesos")
#     precio=700
# else:
#     print("no puede pasar")
    
 
# entradas=0
   
# print("cuantas entradas desea?")
# print("ingrese el total de entradas")
# cantidad=int(input())

# total=cantidad*precio

# print("su total a pagar es", total)


# entradas(int(input("ingrese cuantas entradas desea"))) 



# print("BIENVENIDO A LA SUCURSAL")

# direccion=input("ud pertenece a la comuna de la florida?")

# if direccion == "si":
#     print("puede continuar a la siguiente")
    
    
# carnet=input("ud tiene carnet de socio?")

# if carnet =="si":
#     print=int(input("ingrese su numero de carnet"))
    
    
#---------practica clase del 08 SENTENCIA "FOR"------------

# for i in range(3):
    # print("saludo",i+1)
    
 
 
 
# -------------tablas para modificar-----------   
# num=7 
# for i in range(10):
    # print(num ,"x",i+1,"=",(i+1)*num) 
    
 
#  ----------tabla del 1 al 10------------

# for i in range(1,11):
#     print("tabla de",i)
#     for j in range(1,11):
#         print(i, "X", j, "=", i*j)

    
 
#  USTED TIENE [CANTIDAD DE AÑOS] AÑOS
 

 
# for cantidad_años in range(1,24): 
#     print("usted tiene", cantidad_años, "años")
    


 
    #-----promediar notas----
# total=0
    
# for i in range(3):
#     print("Ingrese una nota")
#     nota=+int(input())
#     total=total+nota
#     print("su promedio es: ", total/(i+1))



# -----------verificacion de numero par o impar----------



# num=int(input("ingrese un numero"))
# for i in range(num+1):
#     if i%2!=0:
#         print("el numero no es par ",i)



# -------para saber cuantas caracteres tiene un texto------

# pal="Hola soy milo"
# print(len(pal))

# for i in pal:
#     print(i)
    
    
# total=0
# nombre=input("ingrese un nombre")
# for i in range(len(nombre)):
#     total=total+(i+1)
# print("el total de la suma de sus numeros es: ", total)
    

    
    
# lista_numeros = [55,79,4,5,6,7,8]


# for valor in lista_numeros:
#     print(valor)
    
    
    
# passw=1234

# for i in range(3):
#     nombre_usuario=input("ingrese su nombre de usuario: ")
#     pas=int(input("ingrese una contraseña:  "))
#     if pas==passw:
#         print("¡BIENVENIDO SEÑOR", nombre_usuario + "!", "INICIANDO SESION...")
#         break
#     else:
#         print("la contraseña no es valida...")
        
# else:
        
#         print("no ha podido ingresar, error")


# # num=64



# for i in range(3):

#     print(f"adivine el numero incognito")
#     cont=int(input("ingrese su numero:  "))
#     print("va en el intento", i+1)
#     if cont==num:
#       print("el numero ingresado es correcto y es: ", num)
#       if cont>=num:
#           print("el numero es mayor, baje un poco mas")
#       if cont<=num:
#             print("su numero es menor, suba un poco mas")
# if i==i:
#     print("ya no hay mas intentos")
# else:
#     print("fin")
        

# if contraseña==1234:
#     print("ha ingresado con exito la contraseña")

#     for contraseña in range(3):
# else:
#         print("error intentelo nuevamente")




# --------------menus-----------



# suma=1
# resta=2
# division=3
# multiplicacion=4
# salir=5


# num1=0
# num2=0

# num3=0
# num4=0

# num5=0
# num6=0

# num7=0
# num8=0


# print("elija una opcion matematica")

# print("suma=1")
# print("resta=2")
# print("division=3")
# print("multiplicacion=4")
# print("salir=5")

# while True:
    
#     op=int(input("ingrese la opcion"))


        
#     if op==(1):
#             print("ud eligio la suma")
#             num1=int(input("ingrese el numero"))
#             num2=int(input("ingrese el segundo numero"))
#             print(num1+num2)
#             print(f"el resultado es:", num1+num2)
            
#     if op==(2):
#             print("ud eligio la resta")
#             num3=int(input("ingrese el numero"))
#             num4=int(input("ingrese el segundo numero"))
#             print(num3-num4)
#             print(f"el resultado es:", num3-num4)
        
#     if op==(3):
#             print("ud eligio la division")
#             num5=int(input("ingrese el numero"))
#             num6=int(input("ingrese el segundo numero"))
#             print(num5/num6)
#             print(f"el resultado es:", num5/num6)
            

#     if op==(4):
#             print("ud eligio la multiplicacion")
#             num7=int(input("ingrese el numero"))
#             num8=int(input("ingrese el segundo numero"))
#             print(num7*num8)
#             print(f"el resultado es:", num7*num8)
#     if op==(5):
#         print("salio del menu")
#         break
            
            
            
            
#     else:
#             print("eliga otra opcion: ")
        




# num=7
# def ver_par():
#         if num>7 and num%2==0:
#             print("el numero es positivo y par")
#         else:
#             print("el numero es positivo e impar")
    
    



# ---------------while-------------------

# num=0

# while num<3:
#     num=num+1
#     print("iteracion", num)


    
    
# comida=100


# while comida!=0:
#     print("aun tiene comida en el plato")
#     print("va a comer una cucharada? (si/no)")
#     verifica=input()
#     if verifica=="si":
#         print("va a comer una cucharada")
#         comida=comida-25
#         print("ud ha sacado: ", comida , '%')
#         if comida==0:
#             print("ud ya se ha terminado toda la comida")
#             break
#         else:
#             print("ud no ha terminado la comida")
    
# ------------ENSAYO DE LA PRUEBA DEL LUNES-------


# 1. Crear un algoritmo que verifique la edad de un usuario y vea el costo del ticket
# print("BIENVENIDO")

# edad_usuario=(int(input("ingrese su edad")))

# if edad_usuario>=10 and edad_usuario<=17:
#     print("El valor del ticket es $1000 pesos")
# elif edad_usuario>=18 and edad_usuario<=64:
#     print("El costo de su ticket es $2000 pesos")
# elif edad_usuario>=65:
#     print("su ticket tiene un valor de $1500")
# else:
#     print("para todos los demas es gratis")
    




# 2. Ingresar 2 número y determinar cuál de ellos es el mayor 
# num1=int(input("ingrese el primer numero"))
# num2=int(input("ingrese el segundo numero"))

# if num1>num2:
#     print(f"el numero mayor de los dos es: {num1}")
# elif num2>num1:
#         print(f"el numero mayor es: {num2}") 
# else:
#         print("Ambos números son iguales")



# 3. Escribe la tabla de multiplicación del 1 al 10 de un número ingresado por pantalla


# num=int(input("ingresar un numero a mostrar para la tabla de * "))
# for i in range(10):
#     print(num ,"x",i+1,"=",(i+1)*num) 




# 4. Realizar un algoritmo que permita llevar el control de las ventas de platos de comida que ofrece el restaurante

# print("bienvenido")

# print("ingresar nombre del cliente=1")
# print("mostrar menu de platos junto con sus precios=2")
# print("mostrar saludo al cliente=3")
# print("salir=4")


# total=0
# precio=0
# resultado=0

# while True:
#     op = int(input("Ingrese una opción: "))

#     if op == 1:
#         cliente = input("Escriba su nombre: ")
#         print("Hola", cliente, "que quiere elegir hoy?, eligiendo la segunda opcion le saldra el menu de platos")
              
        
#     elif op == 2:
#         print("Se mostrará el menú de platos con sus precios:")
#         print("5=Arroz a la francesa $4.500 ")
#         precio1=4500
#         print("6=Arroz marinero $5.200")
#         precio2=5200
#         print("7=Sopa marinera $9.700")
#         precio3=9700
        
#         op2 = int(input("Ingrese una colacion: "))
#         if op2==5:
#             print(f"ud escogio arroz a la francesa y su precio es:{precio1}")
#             print("desea elegir otro plato?")
#             print("para escoger otro plato debe elegir la opcion 2 nuevamente.")

#             total=total+precio1
#             print("su total",total)
#         elif op2==6:
#              print(f"ud escogio arroz marinero y su precio es:{precio2}")
#              print("desea elegir otro plato?")
#              print("para escoger otro plato debe elegir la opcion 2 nuevamente.")

#              total=total+precio2
#              print("su total",total)
#         elif op2==7:
#              print(f"ud escogio sopa marinera y su precio es:{precio3}")
#              print("desea elegir otro plato?")
#              print("para escoger otro plato debe elegir la opcion 2 nuevamente.")

#              total=total+precio3
#              print("su total",total)

        
#     elif op==3:
#         print("Gracias", cliente, "por venir al restorant Panuchis")

#     elif op == 4:
#         print("Salió del programa.")
#         break
            
#     else:
#         print("Vuelva a elegir una opción válida.")




# ---------practica para estudiar en casa prueba--------


# nombre=input("ingrese su nombre: ")
# print("¡Hola", nombre ,"!")

# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética  (3+22⋅5)2

# print(((3+2) / (2*5)) **2)

# print("el resultado es:" , (((3+2) / (2*5)))**2)



# horas_trabajo=int(input("ingresa tus horas trabajadas:  "))
# coste_hora=int(input("ingresa lo que cobras por hora:   "))

# paga = horas_trabajo * coste_hora

# print("tu paga es:", paga)



# ---imc----

# peso_kg=int(input("ingrese su peso aqui:    "))
# estatura_m=int(input("ingrese su estatura aqui: "))

# imc=round(float(peso_kg)/float(estatura_m)**2.2)

# print("tu indice de masa corporal es: "+str(imc))



# ----------------estructura del menu con "match" actividad tarjeta------------

# deuda=100000

# while True:
#     print("""
#           1.-pago de tarjeta credito
#           2.-simulacion de compra
#           3.-salir""")
    
#     op=int(input("ingrese la opcion que quiere escoger: "))
#     match op:
#         case 1:
#             print("su deuda actual es:", deuda)
#             print("ingrese el monto a pagar")
#             pago = int(input("ingrese el pago que desea ingresar:   $"))
#             if pago<=0 or pago>deuda:               #and es para que ambas partes se cumplan y or es para que una sola se pueda cumplir.
#                 print("el pago debe ser mayor a cero y menor que la deuda")
#             else:
#                 deuda=deuda-pago
#             print("El salgo a pagar es: ", deuda)
#         case 2:
#             while True:
#                 print("""seleccione un item
#                     1.-Monitor
#                     2.-Teclado
#                     3.-Laptop
#                     4.-Salir
#                     """)


#                 ops=int(input())
#                 match ops:
#                     case 1:
#                         valor=80000
#                         deuda=valor+deuda
#                         print("Usted añadio un nuevo articulo, su nuevo articulo es: ", deuda)
#                     case 2:
#                         teclado=50000
#                         deuda=valor+deuda
#                         print("Usted añadio un nuevo articulo, su nuevo articulo es: ", deuda)
#                     case 3:
#                         Laptop=1480000
#                         deuda=valor+deuda
#                         print("Usted añadio un nuevo articulo, su nuevo articulo es: ", deuda)
#                     case 4:
#                         print("gracias por su compra")
#                         break
#                     case _:
#                         print("seleccione una opcion valida 1-3")
                        
#         case 3:
#             print("gracias por usar el sistema de credito")
#             break
#         case _:
#             print("seleccione una opcion valida 1-3")


# ---------------definir funciones----------


# def suma():   
#     n1=int(input("ingrese el primer numero:    "))
#     n2=int(input("ingrese el segundo numero:    "))
#     print(n1+n2)
    

# def resta():
#     n1=int(input("ingrese un numero:    "))
#     n2=int(input("ingrese otro numero:  "))
#     print("el resultado es:", n1-n2)
    

# def multi():
#     n1=int(input("ingrese un numero:    "))
#     n2=int(input("ingrese otro numero:  "))
#     print("el resultado es:", n1*n2)
    
    
# def division():
#     n1=int(input("ingrese un numero:    "))
#     n2=int(input("ingrese otro numero:  "))
#     print("el resultado es:", n1/n2)
    
    

    
#     division()
#     resta()
#     suma()
#     multi()



# while True:
#     print("suma=1")
#     print("resta=2")
#     print("multi=3")
#     print("division=4")
#     print("salir=5")
    
    
    
#     op=int(input("ingrese una opcion:   "))
    
#     match op:
#         case 1:
#             suma()
#         case 2:
#             resta()
#         case 3:
#             multi()
#         case 4:
#             division()
#         case 5:
#             print("salir")
#             break
#         case _:
#             print("opcion valida")


# num=6

# if num>0 or num%2==0:
#     print("el numero es positivo y es par")
    
# else:
#     print("el numero no es positivo y no es par")



# n_entrada=564
# entrada=True
# sitioEntrada="platea"


# if n_entrada>300 and entrada==True and sitioEntrada=="platea":
#     print("puede entrar a platea")
# elif n_entrada>300 and entrada==True and sitioEntrada!="platea":
#     print("puede entrar a galeria")
# elif entrada==False:
#     print("no puede entrar")
    
    


# llave="blue"

# if llave=="blue" or llave=="green":
#     print("puede acceder")
# else:
#     print("no puede acceder")
    
    
    
    
# Solicitar un número entero al usuario
# altura = int(input("Introduce un número entero para la altura del triángulo: "))

# # Imprimir el triángulo
# for i in range(1, altura + 1):
#     print('*' * i)



# ----------------actividad de ingresar e iniciar sesion-----------



# usuarios = {}

# def registrar_usuario():

#     if len(usuarios) >= 3:
#         print("Ya se han registrado 3 usuarios")
#         return
    
#     nombre_usuario = input("Ingrese el nombre de usuario (minimo 3 caracteres, maximo 12): ")
#     while len(nombre_usuario) < 3 or len(nombre_usuario) > 12:
#         nombre_usuario = input("Nombre de usuario no válido, Intentelo nuevamente: ")
    
#     contrasena = input("Ingrese la contraseña (minimo 4 caracteres, maximo 10): ")
#     while len(contrasena) < 4 or len(contrasena) > 10:
#         contrasena = input("Contraseña no válida. Intente nuevamente: ")
    
#     usuarios[nombre_usuario] = contrasena
#     print("Usuario registrado con exito.")

# def iniciar_sesion():

#     if not usuarios:
#         print("No hay usuarios registrados, registre usuarios primero...")
#         return
    
#     nombre_usuario = input("Ingrese su nombre de usuario: ")
#     contrasena = input("Ingrese su contraseña: ")
    
#     if usuarios.get(nombre_usuario) == contrasena:
#         print("Inicio de sesion exitoso.")
#     else:
#         print("Nombre de usuario o contraseña incorrectos.")

# def menu():
    
#     while True:
#         print("\n1. Registrar usuario")
#         print("2. Iniciar sesión")
#         print("3. Salir")
        
#         opcion = input("Seleccione una opcion: ")
        
#         if opcion == '1':
#             registrar_usuario()
#         elif opcion == '2':
#             iniciar_sesion()
#         elif opcion == '3':
#             print("El usuario", nombre_usuario, "ha cerrado sesion.....")
#             break
#         else:
#             print("Opción no válida, intentelo nuevamente.")

# if __name__ == "__main__":
#     menu()


# ---------Actividad del juego de ludo---------


# import random

# def dado():
#     return random.randint(1,6)


# def lanzar_dado():
#     return random.randint(1,6)

# print(dado()*2)

# posiciones=[0,0]


# def jugador():
#     return random.randint(1,2)

# print("---------BIENVENIDO AL JUEGO DE LUDO---------")

# print("cuantos jugadores son?")
# jugadores=int(input("indica el numero de jugadores: "))

# print("inicia el juego")

# def mover_jugador(jugador):
#     dado = lanzar_dado()
#     posiciones[jugador] += dado
#     if posiciones[jugador] > 24:
#         posiciones[jugador] = 24
#     print(f"Jugador {jugador + 1} lanzó un {dado} y está en la posición {posiciones[jugador]}")

    

# def hay_ganador():
#     for i, posicion in enumerate (posiciones):
#         if posicion == 24:
#             print(f"¡Jugador {i + 1} ha ganado!")
#             return True or False


# turno = 0
# while not hay_ganador():
#     print(f"Turno del Jugador {turno + 1}")
#     mover_jugador(turno)
#     turno = (turno + 1) % 2

# print("FIN DEL JUEGO")
# print("¡GRACIAS POR JUGAR LUDO EN PYTHON...!")





# -------ACTIVDAD DEL JUEGO DE LUDO 2, clase del 16 de enero---------

# import random

# def lanzar_dado():
#     return random.randint(1, 6)





# jugador1=1
# jugador2=2
# paso=0
# paso2=0

# while True:
    

#     print("---------¡¡¡BIENVENIDOS AL JUEGO DE LUDO!!!---------")

#     print("---------------¡¡¡INICIA EL JUEGO!!!-----------")

#     print("1.- jugador 1")
#     print("2.- jugador 2")
#     print("3.- Salir")
    
#     jugador=int(input("ingrese el jugador que quiere jugar: "))

#     print("le toca al jugador", jugador)
#     print("lanza el dado")
    
#     if jugador==jugador1:
#         lado=lanzar_dado()
#         print(f"el jugador 1 tiró y sacó: {lado}")
#         paso=paso+lado
#         print(f"el jugador 1 esta en la posicion: {paso} de 24")
#         if paso==24:
#             print("ha llegado a la meta")
#             break
#         if paso>=24:
#             paso=24
#             print("ha llegado a la meta")
#             break

#     elif jugador==jugador2:
#         lado=lanzar_dado()
#         print(f"el jugador 2 saco: {lado}")
#         paso2=paso2+lado
#         print(f"el jugador 2 esta en la posicion: {paso2}/24")
#         if paso2==24:
#             print("ha llegado a la meta")
#             break
#         if paso2>=24:
#             paso2=24
#             print("ha llegado a la meta")
#             break
#     elif jugador==3:
#         print("gracias por jugar")
#         break


# -------actividad ruleta rusa-------

# import random

# jugador1=0
# jugador2=0

# def jugador():
#     return random.randint(1,6)


# def ruleta():
#     return random.randint(1,6)

# print("BIENVENIDO A LA RULETA RUSA")

# print("inicio del juego")

# for i in range(6):
#     bala=ruleta()
#     print("es el turno del jugador", i+1)
#     print("Presiona 0 para disparar")
#     disparo=int(input())
#     if disparo==0:
#         if bala==6:
#             print(f"El jugador ha sido finao por la bala {bala}")
#             break
#         else:
#             print("El jugador ha sobrevivido")
#             print("Siguiente turno")
#     else:
#         print("Opcion incorrecta")
#         break



# --------actividad juego pelea----------

# import random

# import time


# #creacion de funcion para la partida

# def partida():

#     player1=60
#     player2=60


#     print("BIENVENIDO AL JUEGO DE PELEAS")

#     print("INICIO DEL JUEGO")



#     print("Turno del jugador 1 para seleccionar el peleador")
#     Nplayer1=input("ingrese el nombre del peleador: ")
#     print("Turno del jugador 2")
#     Nplayer2=input("ingrese el nombre del peleador: ")
#     print("los jugadores comienzan con 60 hp")

#     while True:
    
#         print(f"el {Nplayer1} tiene", player1)
#         print(f"el {Nplayer2} tiene", player2)

#     #ataca el jugador 1

#         ataque1=ataque()
#         print("el jugador 1 ataca con", ataque1)
#         player2=player2-ataque1
#         print("el jugador 2 tiene", player2)
#         time.sleep(1)

#     #ataca el jugador 2
#         ataque2=ataque()
#         print(f"el {Nplayer2} ataca con: ", ataque2)
#         player1=player1-ataque2
#         print(f"el {Nplayer1} tiene", player1)
#         time.sleep(1)

#         if player1<=0:
#             print(f"el {Nplayer1}  ha perdido")
#             break

#         elif player2<=0:
#             print(f"el {Nplayer2} ha perdido")
#             break

        

#         elif player1<=0 and player2<=0:
#             print("EMPATE")
#             break

#         else:
#             print("el juego continua")

# #definicion de ataque por jugador

# def ataque():
#     return random.randint(2,10)

# #inicio de la partida

# partida()



# ----actividad clase del 20 de enero-----

import random

import time


carrito_compras=0


print("*****bienvenido al sistema de ventas******")

print("a continuacion se mostrara el menu de opciones")


while True:
    
    print(""" 
        1.-Productos
        2.-carrito de compras
        3.-medio de pago
        4.-boleta
        5.-salir
          """)


    op=int(input("ingrese una opcion para el menu de opciones a elegir:   "))
        
    match op:
            case 1:
                print("******mostrara los productos disponibles*****")

                print("""
                1. Notebook HP omen: $750.000
                2. Smart TV: $240.000
                3. PS5 Slim:  $600.000
                4. Tablet Samsung: $400.000
                      """)
                
                
                
            case 2:
                
                print("""
                1. Notebook HP omen: $750.000
                2. Smart TV: $240.000
                3. PS5 Slim:  $600.000
                4. Tablet Samsung: $400.000
                      """)
                
                producto=int(input("eliga un producto para el carrito de compras:   "))
                
                if producto==1:
                    print(f"ud ha escogido el Notebook HP omen")
                    carrito_compras=carrito_compras+750000
            
                if producto==2:
                    print("ud ha escogido el Smart TV")
                    carrito_compras=carrito_compras+240000
                    
                if producto==3:
                    print("ud ha escogido el PS5 Slim")
                    carrito_compras=carrito_compras+600000
                    
                if producto==4:
                    print("ud ha escogido la Tablet Samsung")
                    carrito_compras=carrito_compras+400000
                
            case 3:
            
                print("*****METODO DE PAGO*****")
                print("1.-efectivo: sin IVA")
                print("2.-tarjeta de credito: con IVA")
                print("3.-tarjeta debito: con IVA")
                
                op3=int(input("ingrese una opcion para el metodo de pago:   "))
                
                if op3==1:
                    print("ud ha escogido el metodo de pago en efectivo")
                    
                    
                elif op3==2:
                    print("ud ha escogido el metodo de pago con tarjeta de credito")
                    
                    
                elif op3==3:
                    print("ud ha escogido el metodo de pago con tarjeta debito")
                    
            case 4:
                print("boleta")
                print("ud ha escogido la boleta")
                if op3==1:
                    print("el total a pagar es: ", round(carrito_compras))
                elif op3==2:
                    print("pagara con tarjeta credito y el total es: ", round((carrito_compras * 1.19) * 1.0289))
                elif op3==3:
                    print("pagara con tarjeta debito y el total es: ", round((carrito_compras * 1.19)*1.015))
                
            case 5:
                print("SALIENDO DEL PROGRAMA....")
                break          
            case _:
                print("Seleccione una opcion válida")
        
                
            
            
            
        
    
    
    




