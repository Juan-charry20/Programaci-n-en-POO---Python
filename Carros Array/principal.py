from deportivo import Deportivo
from camioneta import Camioneta
from Database import Base_datos
from carro import Carro


#**********************CODIGO PRINCIPAL CARROS****************************
deportivo = Deportivo("Maserati", "rojo", "8.0 Turbo", 2, 2, "Gasolina")
camioneta = Camioneta("Hilux revo", "amarillo", "5.0 Diesel", 4, 5, "Diesel", 1500)

print(deportivo.descripcion())
print(deportivo.aceleracion_frenado())
print(deportivo.info_extra())

print()

print(camioneta.descripcion())
print(camioneta.climatizacion())
print(camioneta.info_extra())

print() 
print()
#**********************CODIGO PRINCIPAL BASE DE DATOS********************************
print()
print()

obj_base_datos = Base_datos()

modelo = input("Ingrese el modelo del vehículo: ")
color = input("Ingrese el color del vehículo: ")
motor = input("Ingrese el tipo de motor: ")
numero_puertas = int(input("Ingrese el número de puertas: "))
capacidad_pasajeros = int(input("Ingrese la capacidad de pasajeros: "))
tipo_combustible = input("Ingrese el tipo de combustible: ")

obj_carro = Carro(modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible)

obj_base_datos.guardar_objeto(obj_carro)

obj_base_datos.imprimir_info()
