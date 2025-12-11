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

    #********* METODOS GETTERS AND SETTERS*******
    # Getters
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_habitat(self):
        return self.habitat

    def get_dieta(self):
        return self.dieta

    def get_tamaño(self):
        return self.tamaño

    def get_color(self):
        return self.color

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_habitat(self, habitat):
        self.habitat = habitat

    def set_dieta(self, dieta):
        self.dieta = dieta

    def set_tamaño(self, tamaño):
        self.tamaño = tamaño

    def set_color(self, color):
        self.color = color