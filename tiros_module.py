#CLASES

class Tiro:
    def __init__(self, serie, tiempo_desc, rep):
        self.serie = serie
        self.tiempo_desc = tiempo_desc
        self.rep = rep


def ingreso_datos_set():

    set1 = Tiro("0", 0, "0")
    set1.serie = int(input("Ingrese el numeros de series: "))
    set1.rep = int(input("Ingrese el numero de repeticiones: "))
    set1.tiempo_desc = float(input("Ingrese el tiempo maximo (minutos): "))

    return set1

def ingreso_datos_cadencia():
    cadencia = input("Ingrese el tipo de cadencia a utilizar DeadStop(D) o Touch N Go(T) : ").capitalize()
    return cadencia

    return suj1

def ingreso_ciclo_pier(x,i,d):

    print("Ingrese la primer pierna a utilizar en el Set N°", x + 1)
    select_pierna = input("Izquierda= I o Derecha= D: ").capitalize()
    print("\n")
    if select_pierna == "I":
        i += 1
    else:
        d += 1

    print("Ingrese la segunda pierna a utilizar en el Set N°", x + 1)

    while True:

        select_pierna = input("Izquierda= I o Derecha= D: ").capitalize()
        print("\n")
        if select_pierna == "D" and i == 1:
            print("Muy bien utilizaste cada pierna en el set")
            break
        if select_pierna == "I" and d == 1:
            print("Muy bien utilizaste cada pierna en el set")
            break
        else:
            print("ERROR, SELECCIONA LA OTRA PIERNA PARA PODER TERMINAR: ")

    return i, d

def ingreso_ciclo_tiemp(set1,snor):

    select_tiempo = float(input("Ingrese el tiempo que tardo en realizar el set (min): "))
    if set1.tiempo_desc >= select_tiempo > 0:
        print("Tu tiempo de descanso fue dentro del rango")
    else:
        print("Y claro powerlifter tenias que ser, para la proxima descansa menos")
        snor += 1

    return snor


def ingreso_ciclo_cadencia(cadencia):
        select_cadencia = input("Ingrese la cadencia realizada en esta serie DeadStop(D) o Touch N Go(T) : ").capitalize()
        if select_cadencia == cadencia:
            print("La cadencia realizada es correcta")
            print("\n------------\n")
        else:
            print("La cadencia no es correcta")

def ingreso_ciclo_rep (set1):
    select_rep = int(input("Ingrese cuantas repeteciones realizo durante este set: "))

    if select_rep != set1.rep :
        if select_rep < set1.rep:
            print("Numero de repeticiones equivocado te faltaron",set1.rep - select_rep, "para completar la serie")
        if select_rep > set1.rep:
            print("Numero de repeticiones equivocado hiciste de mas", select_rep - set1.rep , "repeticiones")
    else:
        print("Numero de repeticiones correcto")


