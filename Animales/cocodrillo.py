from animal import Animal
class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 fuerza_mandibula, acuatico, longitud):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.fuerza_mandibula = fuerza_mandibula
        self.acuatico = acuatico
        self.longitud = longitud

    def cazar(self):
        print(f" el {self.nombre} espera inmóvil antes de atacar.")

    def sumergirse(self):
        print(f" el {self.nombre} se sumerge silenciosamente.")