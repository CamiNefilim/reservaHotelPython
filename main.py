# Importa modulo de fecha
from datetime import datetime

# Importa modulo de tiempo
import time

#Importa clases
from clases import Hotel
from clases.habitacion import HabitacionSimple, HabitacionDoble, Suite

#Importa modulos
from modulos import pedir_fecha, agregar_habitacion, actualiza_habitaciones_disponibles, obtener_habitacion, realizar_reserva, mostrar_comprobante

# Crear un hotel
hotel = Hotel()

# Agregar habitaciones
agregar_habitacion(hotel, HabitacionSimple(101,50000))
agregar_habitacion(hotel, HabitacionDoble(102, 80000))
agregar_habitacion(hotel, Suite(201, 100000))

#Inicia menú reservas
while True:
    print("Menú")
    print("1. Ingresar nueva reserva")
    print("2. Salir")
    opcion = input("Seleccione opción: ")
    
    # Evalúa las opciones
    match opcion:
        case "1":
            print("Para verificar disponibilidad:")
            fecha_ingreso = pedir_fecha("Introduce la fecha de ingreso (YYYY-MM-DD): ")
            fecha_salida = pedir_fecha("Introduce la fecha de salida (YYYY-MM-DD): ")
            actualiza_habitaciones_disponibles(hotel,fecha_ingreso, fecha_salida)  
            
            # Imprime habitaciones disponibles
            print("Las habitaciones disponibles para la fecha son: ")
            
            for hab in hotel.habitaciones_disponibles:
                print(hab)  
            
            while True:
                try:
                    nro = int(input("\n Ingrese el número de habitación a reservar: "))
                    habitacion = obtener_habitacion(nro, hotel)  
                    print(habitacion)              
                    if habitacion:
                        break
                    else:
                        print("El número de habitación no es válido. ")
                except ValueError:
                    # Imprime error
                    print("El número de habitación no es válido. ") 
                
            reserva = realizar_reserva(hotel,habitacion,fecha_ingreso, fecha_salida)  
            mostrar_comprobante(reserva)              
        case "2":
            print("Muchas gracias por usar mi sistema de reserva.")
            break
        case _:
            print("No existe la opción ingresada")
    
    # Espera unos segundos para desplegar el menú
    time.sleep(2)    
