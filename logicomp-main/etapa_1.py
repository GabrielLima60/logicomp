
from formula import *
from functions import *
from semantics import *
import pandas as pd
"""from pysat.solvers import Cadical
from pysat.formula import IDPool"""

# ETAPA 1 USANDO SATISFABILITY_BRUTE_FORCE
"""  
def regras(arquivo):
    df = pd.read_csv(arquivo)
    df = df.drop(index=(df.index[df['P'] == 0]))
    df = df.drop('P', axis= 1)

    

    #é criada uma formula que será sempre falsa e em que serão incluidas outras formulas com conectivos OR
    formulaTotal = Or(Atom('a'),Not(Atom('a')))

    for index, row in df.iterrows():
        #é criada uma formula que será sempre verdadeira e em que serão incluidas outras formulas com conectivos AND
        formulaInterna = And(Atom('a'),Not(Atom('a')))

        for atomica in row.index:
            if row[atomica] == 0:
                formulaInterna = Or(formulaInterna, Not(Atom(atomica)))
            else:
                formulaInterna = Or(formulaInterna, Atom(atomica))
        formulaTotal = And(formulaInterna, formulaTotal)
    if satisfiability_brute_force(formulaTotal):
        return formulaTotal
    else:
        raise Exception("The set of rules is not satistiable")
"""

# ETAPA 2 USANDO PYSAT
def regras(arquivo):
    df = pd.read_csv(arquivo)
    df = df.drop(index=(df.index[df['P'] == 0]))
    df = df.drop('P', axis= 1)
    


    #é criada uma formula que será sempre falsa e em que serão incluidas outras formulas com conectivos OR
    formulaTotal = Or(Atom('a'),Not(Atom('a')))

    for index, row in df.iterrows():
        #é criada uma formula que será sempre verdadeira e em que serão incluidas outras formulas com conectivos AND
        formulaInterna = And(Atom('a'),Not(Atom('a')))

        for atomica in row.index:
            if row[atomica] == 0:
                formulaInterna = Or(formulaInterna, Not(Atom(atomica)))
            else:
                formulaInterna = Or(formulaInterna, Atom(atomica))
        formulaTotal = And(formulaInterna, formulaTotal)
    
    print(formulaTotal.str)

    """grid = list(df.itertuples(index=False))
    var_pool = IDPool()
    solver = Cadical()
    solver.append_formula(formulaTotal)

    if solver.solve():
        solution = solver.get_model()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    for n in range(len(grid)):
                        if var_pool.id(str(i + 1) + '_' + str(j + 1) + '_' + str(n + 1)) in solution:
                            grid[i][j] = n + 1
                            break
        print(grid)
        print('Time to solve:', solver.time())
    else:
        print('Sudoku sem solução!')    
    
"""


print('arquivo 3a_2p: ' + str(regras('column_bin_3a_2p.csv')))
print('\n')
print('arquivo 3a_4p: ' + str(regras('column_bin_3a_4p.csv')))
print('\n')
print('arquivo 3a_5p: ' + str(regras('column_bin_3a_5p.csv')))
print('\n')
print('arquivo 3a_6p: ' + str(regras('column_bin_3a_6p.csv')))
