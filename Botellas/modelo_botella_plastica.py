from modelo_botella import Botella

#creacion de clase hija heredada de clase botella
class Botella_plastico(Botella):

    def __init__(self, marca, capacidad, tapa, diseño ,material, tinte):
        super().__init__(marca, capacidad,tapa)
        self.diseño = diseño
        self.material = material
        self.tinte = tinte
    
    def reciclar_botella(self):
        print (f"la botella se va a reciclar. el material es: {self.material}")

    def imprimir_info(self):
        print (f"el diseo es: {self.diseño}")
        print (f"el material es: {self.material}")
        print (f"el color es: {self.tinte}")
        
        super().imprimir_info()
        print(f"la info de la tapa PADRE es: {self.tapa}")

        return "informacion encontrada"
