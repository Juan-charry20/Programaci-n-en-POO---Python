class Base_datos:
    
    def __init__(self):
        self.lista_carros = []
    
    def guardar_objeto(self, nuevo_objeto):
        self.lista_carros.append(nuevo_objeto)
    
    def agregar_varios_objetos(self):
        self.lista_carros.extend(self.lista_nueva)
    
    def imprimir_info(self):
        for objeto in self.lista_carros:
            print(objeto.get_modelo)
            print(objeto.get_color)
            print(objeto.get_motor)
            print(objeto.get_numero_puertas)
            print(objeto.get_capacidad_pasajeros)
            print(objeto.get_tipo_combustible)