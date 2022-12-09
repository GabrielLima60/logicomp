from formula import *
from functions import *
from semantics import *
from etapa_1 import juntarRegras
from restricoes import *


from pysat.solvers import Cadical
from pysat.formula import CNF

import sys
import time

def satisfabilidade2(arquivo, m):
    
    formula_final = And(And(And(
                juntarRegras(restricao1(arquivo, m)),
                juntarRegras(restricao2(arquivo, m))),
            And(
                juntarRegras(restricao3(arquivo, m)),
                juntarRegras(restricao4(arquivo, m))),),
        juntarRegras(restricao5(arquivo, m)))

    formula_final = CNF(formula_final)
    
    solver = Cadical()
    solver.append_formula(formula_final)
    resultado = solver.solve()

    if resultado == True:
        print('a formula é satisfativel com ' +str(m)+'regras.')

    else:
        print('a formula não é satisfativel com ' +str(m)+'regras.')

    return 0 

satisfabilidade2('/column_bin_3a_2p.csv',2)