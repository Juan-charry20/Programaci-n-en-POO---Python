class Carro:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible


    def encender(self):
        return "El vehículo esta encendido "

    def apagado(self):
        return "El vehículo está apagado "

    def aceleracion_frenado(self):
        return "Puede acelerar y frenar "

    def sistema_direccion(self):
        return "Cuenta con dirección estándar "

    def climatizacion(self):
        return "Sistema de aire acondicionado "

    def tipo_seguridad(self):
        return "Incluye cinturones y frenado combinado "

    def luces(self):
        return "Luces delanteras y traseras "

    def sistema_ventanas(self):
        return "Ventanas manuales o eléctricas "

    def sistema_espejos(self):
        return "Espejos ajustables "

    def descripcion(self):
        return f"Vehículo {self.modelo} color {self.color}, motor {self.motor}."
    
    #********* METODOS GETTERS AND SETTERS*******
    
    # Getters
    def get_modelo(self):
        return self.modelo

    def get_color(self):
        return self.color

    def get_motor(self):
        return self.motor

    def get_numero_puertas(self):
        return self.numero_puertas

    def get_capacidad_pasajeros(self):
        return self.capacidad_pasajeros

    def get_tipo_combustible(self):
        return self.tipo_combustible

    # Setters
    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_color(self, color):
        self.color = color

    def set_motor(self, motor):
        self.motor = motor

    def set_numero_puertas(self, numero_puertas):
        self.numero_puertas = numero_puertas

    def set_capacidad_pasajeros(self, capacidad_pasajeros):
        self.capacidad_pasajeros = capacidad_pasajeros

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible