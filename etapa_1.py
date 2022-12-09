from formula import *
from functions import *
from semantics import *
from restricoes import *

def juntarRegras(restricao):
  formula = restricao[0]
  del restricao[0]
  for f in restricao:
    formula = Or(formula, f)
  return formula




def satisfabilidade(arquivo, m):
  formula_final = And(
        And(
            And(
                juntarRegras(restricao1(arquivo, m)),
                juntarRegras(restricao2(arquivo, m))
            ),
            And(
                juntarRegras(restricao3(arquivo, m)),
                juntarRegras(restricao4(arquivo, m))
            ),
        ),
        juntarRegras(restricao5(arquivo, m))
    )
  s = satisfiability_brute_force(formula_final)

  if s:
      print('a formula é satisfativel com ' +str(m)+'regras.')
  else:
      print('a formula não é satisfativel com ' +str(m)+'regras.')
 

satisfabilidade('/column_bin_3a_2p.csv',2)