import numpy as np

# EJERCICIO 1:

# Matriz de ceros de tipo entero 3x4:
x = np.zeros([3, 4])
print(x)

# Matriz de ceros de tipo entero 3x4 excepto la primera fila que será uno:
x = np.ones([1, 4])
y = np.zeros([2, 4])

w = np.concatenate((a, b), axis=0)
print(w)
 
# Matriz de ceros de tipo entero 3x4 excepto la última fila que será el rango entre 5 y 8:
x = np.arange(5, 9, 1)
y = np.zeros([2, 4])

z = np.concatenate(([a], b), axis=0)
print(z)

# EJERCICIO 2:

# Crea un vector de 10 elementos, siendo los índices impares unos y los índices pares dos:
a = np.one(10)
if np.size(a) % 2 == 0:
    a = np.concatenate((a, np.array([2])))
else : 
    a = np.concatenate((a, np.array([1])))

print(a)

# Crea un «tablero de ajedrez», con unos en las casillas negras y ceros en las blancas:
x = np.array([])
y = np.array([])

while np.size(x) < 8:
    if np.size(x) % 2 == 0:
        x = np.concatenate((x, np.array([0])))
    else:
        a = np.concatenate((a, np.array([1])))

while np.size(y) < 8:
    if np.size(b) % 2 == 0:
        y= np.concatenate((y, np.array([1])))
    else:
        y= np.concatenate((y, np.array([0])))

tab = [x]

fila, columna = np.shape(tab)
while fila < 8:
    if fila % 2 == 0:
        tab = np.concatenate((tab, [y]), axis=0)
        fila, columna = np.shape(tab)
    else:
        tab = np.concatenate((tab, [x]), axis=0)
        fila, columna = np.shape(tab)

print(tab)

#EJERCICIO 3:

# Crea  una  matriz  aleatoria  5x5  y  halla  los  valores mínimo y máximo:

matriz = np.random.rand(5, 5)


vMin = np.min(m)
vMax= np.max(m)

print("el valor minimo es:", vMin)
print("el valor maximo es:",vMax)

# Normalizar la matriz anterior:
 
norma = np.linalg.norm(matriz)
mNorma = matriz/norma
print(" la matriz anterior normalizada sería la sgte: ",mNorma)

