class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def moverse(self):
        print(f"el {self.nombre} se está moviendo.")

    def comunicarse(self):
        print(f" el {self.nombre} se comunica a su manera.")

    def alimentarse(self):
        print(f" el {self.nombre} está comiendo.")

    def descansar(self):
        print(f" el {self.nombre} descansa con tranquilidad.")