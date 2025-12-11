
from carro import Carro

class Deportivo(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.modo_sport = True

    def aceleracion_frenado(self): 
        return "Aceleración rápida y frenado deportivo."

    def info_extra(self):
        return f"Modo sport activo: {self.modo_sport}"