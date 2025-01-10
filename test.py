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
#     pas=int(input("ingrese una contraseña"))
#     if pas==passw:
#         print("bienvenido")
#         break
#     else:
#         print("ha fallado nuevamente")
# else:
        
#         print("no ha podido ingresar, error")


# num=64

# for i in range(3):
#   cont=int(input("ingrese su numero"))
#   if cont==num:
#       print("su numero es correcto el numero es: ", num)
#       break
#       if cont>num:
#           print("el numero es mayor, baje un poco mas")
#       if cont<num:
#             print("su numero es menor, suba un poco mas")
#             if i==i:
#                 print("ya no hay mas intentos")
#       print("fin")
        

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


    
    
comida=100


while comida!=0:
    print("aun tiene comida en el plato")
    print("va a comer una cucharada? (si/no)")
    verifica=input()
    if verifica=="si":
        print("va a comer una cucharada")
        comida=comida-25
        print("ud ha sacado: ", comida , '%')
        if comida==0:
            print("ud ya se ha terminado toda la comida")
            break
        else:
            print("ud no ha terminado la comida")
    
