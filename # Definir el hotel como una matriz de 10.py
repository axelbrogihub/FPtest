# Definimos la matriz para el hotel, 10 pisos y 6 habitaciones por piso
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
