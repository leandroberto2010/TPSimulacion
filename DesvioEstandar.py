import random
import sys
import numpy as np
import matplotlib.pyplot as plt

#------Generar de datos----------
std_devs = []  
 

YY = 1  #Cantidad de analisis
XXX = 100 #Cantidad de tiradas

values=[]
for _ in range(YY): #Cantidad de analisis
    
    for _ in range (XXX):
        curVal = random.randint(0, 36) #current value
        values.append(curVal)
        std_devs.append(np.std(values))        
    
    


#------Graficar----------
plt.plot(range(len(std_devs)), std_devs, marker='o', linestyle='-')
plt.xlabel('Análisis')
plt.ylabel('Desvío Estándar')
plt.title('Desvío Estándar')
plt.grid(True)
plt.show()