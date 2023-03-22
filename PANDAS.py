import pandas as pd
import os 
import glob

a =os.getcwd()
print(a)
file = glob.glob(a+'/*.csv')
print(file)

mmse = pd.read_csv(file[0],sep =';')
print (mmse)
#print(mmse['Escolaridad']) #imprime la columna sin el titulo(escolariad)
#print(mmse['Escolaridad'].describe) # nos da las estadisticas de la columna 
mmse_codigo=mmse
mmse_codigo = mmse_codigo.set_index('Codigo')# le asigno al index el numero del codigo 
print(mmse_codigo)
print("hola")
h = mmse_codigo.loc["CTR_001"] #busco un sujeto por si index LITERAL
print(h)
d = mmse_codigo.iloc[3] # busco un sujeto por su posicion en ENTERO
print(d)