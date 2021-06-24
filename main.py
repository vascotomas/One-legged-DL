"""" La consigna ya la tenes, la pauta es que tiene que ser un codigo que reconozca que pierna va a laburar,
la cadencia de los tiros, que pasa si esta bien, que pasa si esta mal.
Tiene que contemplar el tiempo de descanso entre sets, los sets, y las reps.
Ah, y no te tiene que permitir volver a tirar con la misma pierna si ya tiraste """


from tiros_module import Tiro
from tiros_module import ingreso_datos_set, ingreso_datos_cadencia
from tiros_module import ingreso_ciclo_pier, ingreso_ciclo_tiemp, ingreso_ciclo_cadencia, ingreso_ciclo_rep


print("Bienvenido, ingrese como sera su Set \n")

set1 = Tiro

set1 = ingreso_datos_set()
cadencia = ingreso_datos_cadencia()


################

print('\n'*80)

# CORROBORA SERIE POR SERIE Y PIERNA POR PIERNA
i = 0
d = 0
snor = 0

for x in range(0, set1.serie):

    i, d = ingreso_ciclo_pier(x, i, d)
    i = 0
    d = 0
    print("------------------------------------------------")
    ingreso_ciclo_rep(set1)
    print("------------------------------------------------")
    snor = ingreso_ciclo_tiemp(set1, snor)
    print("------------------------------------------------")
    ingreso_ciclo_cadencia(cadencia)
    print("------------------------------------------------")

print("\n####################################################\n")

if snor == 0:
    print("\nCompletaste las series")

else:
    print("\nCompletaste las series satisfactoriamente. Pero te convertiste en un Snorlax")
