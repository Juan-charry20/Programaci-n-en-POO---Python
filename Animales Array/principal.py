from caballo import Caballo
from cocodrillo import Cocodrilo
from pez import Pez
from escarabajorinoceronte import EscarabajoRinoceronte
from pato import Pato
from Database import Base_datos
from animal import Animal

#**********************CODIGO PRINCIPAL ANIMALES****************************
caballo = Caballo("caballo", 5, "pradera", "pasto", "grande", "blanco", 60, "liso", True)
caballo.galopar()

croc = Cocodrilo("cocodrilo", 12, "río", "carnívoro", "grande", "verde", 2000, True, 4.5)
croc.sumergirse()

pez = Pez("pez payaso", 1, "arrecife", "plancton", "pequeño", "azul", 35, "redonda", True)
pez.nadar()

esc = EscarabajoRinoceronte("escarabajao", 2, "selva", "savia", "pequeño", "negro", 850, "duro", 3)
esc.excavar()

pato = Pato("patito feo", 3, "lago", "omnivoro", "mediano", "verde",0.75, True, "hidrofóbico")
pato.nadar()

print()
print()
#**********************CODIGO PRINCIPAL BASE DE DATOS********************************
print()
print()

obj_base_datos = Base_datos()

nombre = input("Ingrese el nombre para su animal: ")
edad = input("Ingrese la edad del animal: ")
habitat = input("Ingrese donde habita: ")
dieta = input("Ingrese la dieta del animal: ")
tamaño = input("Ingrese el tamaño del animal: ")
color = input("Ingrese el color del animal: ")
obj_animal = Animal(nombre, edad, habitat, dieta, tamaño, color)

obj_base_datos.guardar_objeto(obj_animal)
obj_base_datos.imprimir_info()
