from modelo_botella import Botella
from modelo_botella_plastica import Botella_plastico
from Database import Base_datos
from botella import botella

#**********************CODIGO PRINCIPAL MODELOS DE BOTELLAS****************************

#instancia del padre
objBotella = Botella("Coca-Cola", "1.5L", "Especial")
objBotella.imprimir_info()

#instancia de la hija
objBotella_plastica = Botella_plastico("pepsi", "2.5L", "comun", "redondo", "plastico", "sin tinte")
dato = objBotella_plastica.imprimir_info()
print(dato)

print() 
print()
#**********************CODIGO PRINCIPAL BASE DE DATOS********************************
print()
print()

obj_base_datos = Base_datos()

codigo = input("Ingrese el codigo de la botella: ")
color = input("Ingrese el color de la botella: ")
obj_botella = botella(codigo, color)

obj_base_datos.guardar_objeto(obj_botella)

obj_base_datos.imprimir_info()
