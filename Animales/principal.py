from caballo import Caballo
from cocodrillo import Cocodrilo
from pez import Pez
from escarabajorinoceronte import EscarabajoRinoceronte
from pato import Pato

def principal():
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


if __name__ == "__main__":
    principal()