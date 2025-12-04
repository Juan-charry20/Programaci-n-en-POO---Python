from animal import Animal
class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 envergadura, migratorio, tipo_plumaje):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.envergadura = envergadura
        self.migratorio = migratorio
        self.tipo_plumaje = tipo_plumaje

    def nadar(self):
        print(f" el {self.nombre} se desliza sobre el agua.")

    def volar(self):
        print(f"el {self.nombre} emprende vuelo con elegancia.")