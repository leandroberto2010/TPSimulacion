import random
import numpy as np
import matplotlib.pyplot as plt

#------Generar de datos----------
frecuencias = []

XXX = 100  # Representa el número de tiradas que se realizarán en cada corrida de la simulación.
YYY = 15   # Representa el número de corridas que se realizarán en la simulación.
X = 2     # Representa el número que el usuario elige como objetivo en la simulación.

# Calcular las frecuencias relativas para cada tirada
values = []              
for _ in range(XXX):  # Total de tiradas
    curVal = random.randint(0, 36)  
    values.append(curVal)
    freq = values.count(X) / len(values)  # Calcular la frecuencia relativa con respecto a X para cada tirada
    frecuencias.append(freq)  # Agregar la frecuencia relativa de la tirada actual

yl = yl = np.mean(frecuencias)  
 
plt.axhline(y=yl, color='r', linestyle='--')

# Graficar la frecuencia relativa con respecto a X en función del número de tiradas
plt.plot(range(len(frecuencias)), frecuencias, marker='o', linestyle='-')
plt.xlabel('Número de Tiradas')
plt.ylabel('Frecuencia Relativa con respecto a {}'.format(X))
plt.title('Frecuencia Relativa con respecto a {}'.format(X))
plt.grid(True)
plt.show()


