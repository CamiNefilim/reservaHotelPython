from datetime import datetime

class Habitacion:
    def __init__(self, numero, precio_por_noche):
        self.numero = numero
        self.precio_por_noche = precio_por_noche

    def __str__(self):
        return f"Habitación {self.numero} - Precio por Noche: {self.precio_por_noche}"
    
# Subclases para cada tipo de habitación

class HabitacionSimple(Habitacion):
    def __init__(self, numero, precio_por_noche):
        super().__init__(numero, precio_por_noche)
        self.tipo = "Simple"

    def __str__(self):
        return f"Habitación {self.numero} - Tipo: {self.tipo} - Precio por Noche: {self.precio_por_noche}"

class HabitacionDoble(Habitacion):
    def __init__(self, numero, precio_por_noche):
        super().__init__(numero, precio_por_noche)
        self.tipo = "Doble"

    def __str__(self):
        return f"Habitación {self.numero} - Tipo: {self.tipo} - Precio por Noche: {self.precio_por_noche}"

class Suite(Habitacion):
    def __init__(self, numero, precio_por_noche):
        super().__init__(numero, precio_por_noche)
        self.tipo = "Suite"
    
    def __str__(self):
        return f"Habitación {self.numero} - Tipo: {self.tipo} - Precio por Noche: {self.precio_por_noche}"
