import random
import sys
import numpy as np
import matplotlib.pyplot as plt



XXX= int(sys.argv[1])
YYY= int(sys.argv[2])
X= int(sys.argv[3])

for _ in range(YYY): #Cantidad de analisis
    #------Generar de datos----------
    std_devs = []
    frecuencias = []
    promedios = []
    varianzas = [] 
    values=[]
 
    
    for _ in range (XXX):
        curVal = random.randint(0, 36) #current value
        values.append(curVal)
        std_devs.append(np.std(values))  
        freq = values.count(X) / len(values)  # Calcular la frecuencia relativa con respecto a X para cada tirada
        frecuencias.append(freq)  # Agregar la frecuencia relativa de la tirada actual
        promedios.append(np.mean(values))
        varianzas.append(np.var(values))

    
    yd = np.mean(std_devs)
    yf = 0.027
    yp = np.mean(promedios)
    yv = np.mean(varianzas)       
        
        


    #------Graficar----------
    # Añadir una línea horizontal

    fig, axs = plt.subplots(2, 2)
    # Graficar en el primer subgráfico
    axs[0, 0].axhline(y=yd, color='r', linestyle='--')
    axs[0, 0].plot(range(len(std_devs)), std_devs, linestyle='-')
    axs[0, 0].set_xlabel('n (numero de tiradas)')
    axs[0, 0].set_ylabel('Desvío Estándar')
    #axs[0, 0].set_title('Desvío Estándar')
    axs[0, 0].grid(True)

    #Segundo grafico
    axs[0, 1].axhline(y=yf, color='r', linestyle='--')
    axs[0, 1].plot(range(len(frecuencias)), frecuencias, 'tab:orange', linestyle='-')
    axs[0, 1].set_xlabel('n (numero de tiradas)')
    axs[0, 1].set_ylabel('Frecuencia relativa respecto a :{}'.format(X))
    #axs[0, 1].set_title('Frecuencia Relativa con respecto a {}'.format(X))
    axs[0, 1].grid(True)

    #Tercer grafico
    axs[1, 0].axhline(y=yp, color='r', linestyle='--')
    axs[1, 0].plot(range(len(promedios)), promedios, 'tab:green', linestyle='-')
    axs[1, 0].set_xlabel('n (numero de tiradas)')
    axs[1, 0].set_ylabel('Valor promedio de las tiradas')
    #axs[1, 0].set_title('Promedios')
    axs[1, 0].grid(True)

    #Cuarto grafico
    axs[1, 1].axhline(y=yv, color='r', linestyle='--')
    axs[1, 1].plot(range(len(varianzas)), varianzas, 'tab:red', linestyle='-')
    axs[1, 1].set_xlabel('n (numero de tiradas)')
    axs[1, 1].set_ylabel('Varianzas')
    #axs[1, 1].set_title('Varianzas')
    axs[1, 1].grid(True)

    # Mostrar la figura
    plt.show()

    #Graficos superpuestos
    