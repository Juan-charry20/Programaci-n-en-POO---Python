class Botella():
    def __init__(self, marca, capacidad, tapa):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa

    def llenar_botella(self,capacidad):
        print(f"la botella se esta llenando:{capacidad}")
        print(f"Se va a usar la tapa:{self.tapa}")

    def cerrar_tapa(self, dato_cantidad):
        print(f"Se uso la tapa:{self.tapa}")
        print(f"Cantidad de tapas usadas:{dato_cantidad}")
        return dato_cantidad
    
    #******METODO IMPRIME LA INFORMACION DE LOS ATRIBUTOS*******
    def imprimir_info(self):
        print(f"la marca es: {self.marca}")
        print(f"el tipo de tapa es: {self.tapa}")
        print(f"la capacidad de la botella es: {self.capacidad}") 
        