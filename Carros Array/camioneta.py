from carro import Carro

class Camioneta(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible, capacidad_carga_kg):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.capacidad_carga_kg = capacidad_carga_kg

    def climatizacion(self):  
        return "Climatización básica para cabina de trabajo."

    def info_extra(self):
        return f"Capacidad de carga: {self.capacidad_carga_kg} kg"