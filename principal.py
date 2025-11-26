from modelo_botella import Botella
from modelo_botella_plastica import Botella_plastico

#**********************CODIGO PRINCIPAL****************************

#instancia del padre
objBotella = Botella("Coca-Cola", "1.5L", "Especial")
objBotella.imprimir_info()

#instancia de la hija
objBotella_plastica = Botella_plastico("pepsi", "2.5L", "comun", "redondo", "plastico", "sin tinte")
dato = objBotella_plastica.imprimir_info()
print(dato)
