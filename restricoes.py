from formula import *
from functions import *
from semantics import *
import pandas as pd

def restricao1(arquivo, m):
  df = pd.read_csv(arquivo)
  df = df.drop(index=(df.index[df['P'] == 0]))
  df = df.drop('P', axis= 1)

  total = []
  for parametro in range(m):
    for index, row in df.iterrows():
        formula = Or (Or(And(
                            And(Atom('X_' + str(row.index[0]) + ',' + str(parametro+1) + ',p'), Not(Atom('X_' + str(row.index[0]) + ',' + str(parametro+1) + ',n'))),
                            Not(Atom('X_' + str(row.index[0]) + ',' + str(parametro+1) + ',s'))),
                        And(
                            And(Not(Atom('X_' + str(row.index[0]) + ',' + str(parametro+1) + ',p')), Atom('X_' + str(row.index[0]) + ',' + str(parametro+1) + ',n')),
                            Not(Atom('X_' + str(row.index[0]) + ',' + str(parametro+1) + ',s'))),),
                      And(
                        And(Not(Atom('X_' + str(row.index[0]) + ',' + str(parametro+1) + ',p')), Not(Atom('X_' + str(row.index[0]) + ',' + str(parametro+1) + ',n'))),
                        Atom('X_' + str(row.index[0]) + ',' + str(parametro+1) + ',s')))
        row.index.drop(row.index[0])
        for j in range(len(row.index)):
            formula = Or (Or(And(
                            And(Atom('X_' + str(row.index[j]) + ',' + str(parametro+1) + ',p'), Not(Atom('X_' + str(row.index[j]) + ',' + str(parametro+1) + ',n'))),
                            Not(Atom('X_' + str(row.index[j]) + ',' + str(parametro+1) + ',s'))),
                        And(
                            And(Not(Atom('X_' + str(row.index[j]) + ',' + str(parametro+1) + ',p')), Atom('X_' + str(row.index[j]) + ',' + str(parametro+1) + ',n')),
                            Not(Atom('X_' + str(row.index[j]) + ',' + str(parametro+1) + ',s'))),),
                      And(
                        And(Not(Atom('X_' + str(row.index[j]) + ',' + str(parametro+1) + ',p')), Not(Atom('X_' + str(row.index[j]) + ',' + str(parametro+1) + ',n'))),
                        Atom('X_' + str(row.index[j]) + ',' + str(parametro+1) + ',s')))
        total.append(formula)
  return(total)


def restricao2(arquivo,m):
    df = pd.read_csv(arquivo)
    df = df.drop(index=(df.index[df['P'] == 0]))
    df = df.drop('P', axis= 1)

    total = []
    for i in range(m):
      for index, row in df.iterrows():
          formula = Not(Atom('X_'+str(row.index[0])+','+str(i+1)+',s'))
          row.index.drop(row.index[0])
          for j in range(len(row.index)):
              formula = Or(formula, Not(Atom('X_'+str(row.index[j])+','+str(i+1)+',s')))
      total.append(formula)
    return(total)


def restricao3(arquivo,m):
    df = pd.read_csv(arquivo)
    df = df.drop(index=(df.index[df['P'] == 1]))
    df = df.drop('P', axis= 1)

    total = []
    
    for index, row in df.iterrows():
      paciente = []
      for parametro in range(m):          
          if row[row.index[0]] == 0:
            formula = Atom('X_'+str(row.index[0])+','+str(parametro+1)+',le')
          else:
            formula = Atom('X_'+str(row.index[0])+','+str(parametro+1)+',gt')

          for j in range(len(row.index)):
              if j == 0:
                pass
              else:
                if row[row.index[j]] == 0:
                  formula = Or(formula, Atom('X_'+str(row.index[j]+','+str(parametro+1)+',le')))
                else:
                  formula = Or(formula, Atom('X_'+str(row.index[j]+','+str(parametro+1)+',gt')))
          total.append(formula)  
    return(total)


def restricao4(arquivo,m):
    df = pd.read_csv(arquivo)
    df = df.drop(index=(df.index[df['P'] == 0]))
    df = df.drop('P', axis= 1)

    total = []
    numeroPaciente = 0
    for index, row in df.iterrows():
      numeroPaciente+=1
      for parametro in range(m):          
          if row[row.index[0]] == 0:
            formula = Implies(Atom('X_'+str(row.index[0])+','+str(parametro+1)+',le'), Not(Atom('C_'+str(parametro+1)+','+str(numeroPaciente)))) 
          else:
            formula = Implies(Atom('X_'+str(row.index[0])+','+str(parametro+1)+',gt'), Not(Atom('C_'+str(parametro+1)+','+str(numeroPaciente)))) 

          for j in range(len(row.index)):
              if j == 0:
                pass
              else:
                if row[row.index[j]] == 0:
                  formula = And(formula, Implies(Atom('X_'+str(row.index[j]+','+str(parametro+1)+',le')), Not(Atom('C_'+str(parametro+1)+','+str(numeroPaciente))))) 
                else:
                  formula = And(formula, Implies(Atom('X_'+str(row.index[j]+','+str(parametro+1)+',gt')), Not(Atom('C_'+str(parametro+1)+','+str(numeroPaciente))))) 
          total.append(formula)  
    return(total)


def restricao5(arquivo,m):
    df = pd.read_csv(arquivo)
    df = df.drop(index=(df.index[df['P'] == 0]))
    df = df.drop('P', axis= 1)

    total = []
    numeroPaciente = 0
    for index, row in df.iterrows():
       numeroPaciente+=1
       paciente = []
       formula = Atom('C_1'+','+str(numeroPaciente))
       for parametro in range(m):
          if parametro == 0:
            pass
          else:          
            formula = Or(formula,Atom('C_'+str(parametro+1)+','+str(numeroPaciente)))
       total.append(formula)  
    return total
