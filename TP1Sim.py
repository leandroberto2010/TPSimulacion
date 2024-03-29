import random
import sys
import matplotlib.pyplot as plt

"""# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 3 or sys.argv[1] != "-n":
    print("Uso: python programa.py -n <num_valores>")
    sys.exit(1)

# Obtener el número de valores de los argumentos de la línea de comandos
num_valores = int(sys.argv[2])"""
#Ingreso por consola de parámetros para la simulación (cantidad de tiradas, corridas y número elegido, Ejemplo python -c XXX -n YYY -e ZZ).

"""
Para permitir que los usuarios ingresen los parámetros por la consola en un programa Python, se debe utilizar 
el módulo "argparse", que facilita el análisis de argumentos de línea de comandos. 
import argparse
"""



values=[]

def abs_freq(x):
  abs = [(value, x.count(value)) for value in set(x)]
  return abs

def rel_freq(x):
  freqs = [(value, x.count(value)/len(x)) for value in set(x)]
  return freqs

"""def calc_avg(x):
    for _ in x:
       sum = sum+x
    avg = sum/len(x)
    return avg"""

for _ in range (10000):
  curVal = random.randint(0, 36) #current value
  values.append(curVal)
  print(curVal)

print(rel_freq(values))
print(abs_freq(values))
#print(calc_avg(values))

# Separar los valores y las frecuencias
values1, frequencies = zip(*rel_freq(values))

# Crear el gráfico de barras
plt.bar(values1, frequencies)

# Añadir una línea horizontal en y = 0.5 (por ejemplo)
plt.axhline(y=0.027, color='r', linestyle='--')

# Ajustar el aspecto del gráfico
plt.xlabel('Valor')
plt.ylabel('Frecuencia Relativa')
plt.title('Gráfico de Frecuencias Relativas')
plt.grid(True)

# Mostrar el gráfico
plt.show()







