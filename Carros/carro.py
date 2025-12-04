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