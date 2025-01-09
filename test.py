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


num=64

for i in range(5):
    cont=(1,5)
    num=int(input("ingrese el numero desconocido"))
if num<=64:
    print("su numero es muy bajo")
if num>=64:
    print("su numero es muy alto")
elif num==64:
    print("FELICIDADES!")
else:
    print("intente nuevamente")

        
        
        

# if contraseña==1234:
#     print("ha ingresado con exito la contraseña")

#     for contraseña in range(3):
# else:
#         print("error intentelo nuevamente")