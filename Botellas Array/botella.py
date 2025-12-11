class botella:
    def __init__(self, codigo, color):
        self.codigo = codigo
        self.color = color
    
    def get_codigo(self):
        return self.codigo
    
    def set_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo

    def get_color (self):
        return self.color
    
    def set_color (self, nuevo_color):
        self.color = nuevo_color
