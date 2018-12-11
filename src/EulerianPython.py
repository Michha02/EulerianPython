import time
import sys
from src import Eulerian

flagt = False
flagm = False

for i in sys.argv:
    if i == "-t":
        if flagt:
            print ("No se pueden repetir los flags")
            exit(1)
        else:
            flagt = True

    elif i == "-m":
        if flagm:
            print ("No se pueden repetir los flags")
            exit(2)
        else:
            flagm = True

    elif i[0] == "-":
        print ("La flag " + i + " no es válida")
        exit(3)

if flagm:
    print ("Se va a calcular mediante memorization")
else:
    print ("Se va a calcular mediante tabulation")

start_time = time.time()
f = open(sys.argv[len(sys.argv)-1])
for linea in f:
    n = int(linea[0:linea.index(" ")])
    m = int(linea[linea.index(" "):len(linea)])
    if m >= n:
        print ("No se puede hacer la operación porque en " + "n=" + str(n) + " y m=" + str(m) + " n < m")
    elif m < 0:
        print("No se puede hacer la operación con números negativos")
    else:
        if flagm:
            print("n=" + str(n) + ", m=" + str(m) + "; Eulerian Number=" + str(Eulerian.eulerianmem(n, m)))
        else:
            print("n=" + str(n) + ", m=" + str(m) + "; Eulerian Number=" + str(Eulerian.euleriantab(n, m)))

if flagt:
    print("Ejecución terminada en " + str(time.time() - start_time) + " segundos")



