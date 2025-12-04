from animal import Animal
class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                velocidad_maxima, tipo_pelaje, domestico):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.velocidad_maxima = velocidad_maxima
        self.tipo_pelaje = tipo_pelaje
        self.domestico = domestico

    def galopar(self):
        print(f" el {self.nombre} galopa a {self.velocidad_maxima} km/h.")

    def paseando(self):
        print(f" el {self.nombre} está paseando en el campo.")