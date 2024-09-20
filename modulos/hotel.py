from clases import Hotel, Reserva

def agregar_habitacion(hotel, habitacion):
    hotel.habitaciones.append(habitacion)
    
def habitacion_disponible(hotel, habitacion, fecha_ingreso, fecha_salida):
    # Verificamos si la habitación tiene una reserva que se superpone con las fechas dadas
    for reserva in hotel.reservas:
        if reserva.habitacion == habitacion:
            if not (fecha_salida <= reserva.fecha_ingreso or fecha_ingreso >= reserva.fecha_salida):
                return False  # Si hay superposición, la habitación no está disponible
    return True  # Si no hay superposición, la habitación está disponible

def actualiza_habitaciones_disponibles(hotel, fecha_ingreso, fecha_salida):
    # Filtrar habitaciones disponibles
    hotel.habitaciones_disponibles = [hab for hab in hotel.habitaciones if habitacion_disponible(hotel, hab, fecha_ingreso, fecha_salida)]
    
def obtener_habitacion(nro, hotel):
    for habitacion in hotel.habitaciones_disponibles:
        print(habitacion.numero)
        print(nro)
        if(habitacion.numero == nro):
            print("si")
            return habitacion
    return None

def realizar_reserva(hotel, habitacion, fecha_ingreso, fecha_salida):
    noches = calcular_noches(fecha_ingreso, fecha_salida)
    total = calcular_total(habitacion, noches)
    reserva = Reserva(habitacion, fecha_ingreso, fecha_salida, noches, total)
    hotel.reservas.append(reserva)
    return reserva

def calcular_noches(fecha_ingreso, fecha_salida):
        delta = fecha_salida - fecha_ingreso
        return delta.days

def calcular_total(habitacion, noches):
    return habitacion.precio_por_noche * noches

def mostrar_comprobante(reserva):
        print("\n--- Comprobante de Reserva ---")
        print(f"Habitación: {reserva.habitacion.numero} - Tipo: {reserva.habitacion.tipo}")
        print(f"Fecha de ingreso: {reserva.fecha_ingreso.strftime('%Y-%m-%d')}")
        print(f"Fecha de salida: {reserva.fecha_salida.strftime('%Y-%m-%d')}")
        print(f"Número de noches: {reserva.noches}")
        print(f"Costo total: ${reserva.total:.2f}")
        print("--- Gracias por su preferencia ---\n")
