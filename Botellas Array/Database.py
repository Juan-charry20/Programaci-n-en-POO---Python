class Base_datos:

    def __init__(self):
        self.lista_botellas = []
        self.lista_plastico = []
    
    def guardar_objeto(self, nuevo_objeto):
        self.lista_botellas.append(nuevo_objeto)
    
    def agregar_varios_objetos(self):
        self.lista_botellas.extend(self.lista_nueva)

    def imprimir_info(self):
        for objeto in self.lista_botellas:
            print(objeto.get_color)
            print(objeto.get_codigo)