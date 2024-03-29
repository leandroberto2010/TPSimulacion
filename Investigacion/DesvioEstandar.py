import random
import sys
import numpy as np
import matplotlib.pyplot as plt

#------Generar de datos----------
std_devs = []  
 

XXX=100 # Representa el número de tiradas que se realizarán en cada corrida de la simulación.
YYY=1 #Representa el número de corridas que se realizarán en la simulación.
#ZZ  Representa el número que el usuario elige como objetivo en la simulación.

yl=0
values=[]
for _ in range(YYY): #Cantidad de analisis
    
    for _ in range (XXX):
        curVal = random.randint(0, 36) #current value
        values.append(curVal)
        std_devs.append(np.std(values))  
    
yl = np.mean(std_devs)       
    
    


#------Graficar----------
# Añadir una línea horizontal
plt.axhline(y=yl, color='r', linestyle='--')

plt.plot(range(len(std_devs)), std_devs, marker='o', linestyle='-')
plt.xlabel('n (numero de tiradas)')
plt.ylabel('Desvío Estándar')
plt.title('Desvío Estándar')
plt.grid(True)
plt.show()