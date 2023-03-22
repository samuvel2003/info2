import numpy as np
import pandas as pd
import os 
import glob
### ARCHIVO MMSE ###
a =os.getcwd()
print(a)
file = glob.glob(a+'/*.csv')
#print(file)
mmse = pd.read_csv(file[0],sep =';')
#print (mmse)
mmse_edad = mmse.sort_values(by="Edad en la visita")# organizo la columna de menor a mayor
mmse_o=mmse_edad.reset_index()# reinicio el index para que me coincida index 0 con el de menor edad 
mmse_o=mmse_o.drop(columns=["index"])#elimino el index anterior 
#print(mmse_o)

### ARCHIVO EVALUACIONMEDICA ###
b = os.getcwd()
file2 = glob.glob(b+'/*.xlsx')
eva_med = pd.read_excel(file2[0])
eva_med_edad = eva_med.sort_values(by = 'Edad en la visita')
eva_med_o = eva_med_edad.reset_index()
eva_med_o = eva_med_o.drop(columns = ['index'])
print(eva_med_o)

#if eva_med['Codigo'] == mmse_o['Codigo']:

union = pd.merge(eva_med_o,mmse_o, on = ['Codigo', 'Sexo', 'Edad en la visita'])
print ( union.columns.values)


