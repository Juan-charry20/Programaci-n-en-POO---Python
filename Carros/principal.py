from deportivo import Deportivo
from camioneta import Camioneta

def main():
    deportivo = Deportivo("Maserati", "rojo", "8.0 Turbo", 2, 2, "Gasolina")
    camioneta = Camioneta("Hilux revo", "amarillo", "5.0 Diesel", 4, 5, "Diesel", 1500)

    print(deportivo.descripcion())
    print(deportivo.aceleracion_frenado())
    print(deportivo.info_extra())

    print()

    print(camioneta.descripcion())
    print(camioneta.climatizacion())
    print(camioneta.info_extra())

main()