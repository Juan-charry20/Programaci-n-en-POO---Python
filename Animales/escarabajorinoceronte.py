from animal import Animal
class EscarabajoRinoceronte(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 fuerza_relativa, exoesqueleto, longitud_cuerno):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.fuerza_relativa = fuerza_relativa
        self.exoesqueleto = exoesqueleto
        self.longitud_cuerno = longitud_cuerno

    def excavar(self):
        print(f" el {self.nombre} excava con determinación.")

    def levantar(self):
        print(f" el {self.nombre} demuestra su fuerza impresionante.")