import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
print(a.data)
print(a.dtype.name)
print(a.itemsize)

c = np.array([[1, 2], [3, 4]], dtype=complex)
print('\n', c)
np.concatenate(x,y)# une los arreglos en uno solo(x,y son arrays)
c.ndim# dimension del arreglo
c.shape# filas y columnas del array
c.size # cantidas de obajetos en el array

# generador para la clase de numeros aleatorios: default_rng
rg= np.random.defaul_rng(seed = None )
g = rg.random((3,4))#3: num de filas, 4: columnas
np.floor
np.hstack # concatenacion horizontal
np.vstack # concatenacion vertical 
# tambien nos proporciona funciones matamaticas como sen, cos, suma, resta, multiplicacion, division...

