
import random
import sys
import numpy as np
import matplotlib.pyplot as plt

#------------------------------Constantes---------------------------------------------------
s = "m" #La estrategia utilizada: m (martingala), d (D’Alambert), f (Fibonacci) y o (Suicida)
a = "f" #El tipo de capital: i (infinito), f (finito).
YYY=1
XXX=1000

cfi = 100  #Cafital finito inicial
ci = "Auto" #Color inicial "R" (Rojo), "V" (Verde), "N" (Negro), "Auto" (Automatico)
#-------------------------------------------------------------------------------------------

capital_money=[]
chosen_colors=[]


def tipocapital(a):
    if(a=="i"):
        return float('inf')
    else:
        global cfi
        return cfi


def jugar(n): #Estrategia por color
    rojos={1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    
    na = random.randint(0, 36)
    color_na = ""
    color_n = ""
    if (na in rojos):
        color_na = "R"
    elif na == 0:
        color_na = "V"
    else:
        color_na = "N"
    chosen_colors.append(color_na)
    

  
    global ci #Color inicial
    if(ci=="R"):
        color_n = "R"
    elif(ci=="V"):
        color_n = "V"
    elif(ci=="N"):
        color_n = "N"
    else:
        if chosen_colors:
            counts = {color: chosen_colors.count(color) for color in {"R", "V", "N"}}
            color_n = max(counts, key=counts.get)
        else:
            color_n = "R"
    return color_n == color_na

  #Siempre al doble y si ganas vuelves a empezar
def martingala(): 
    
    
    p = tipocapital(a)   # Presupuesto inicial
    apuesta = 1    # Apuesta inicial
    global XXX
    r=0
    while p >= apuesta and XXX != r:
        r +=1
        capital_money.append(p)
        resultado = jugar(apuesta)
        print(f"Presupuesto: {p}, Apuesta: {apuesta}, Resultado: {'Gana' if resultado else 'Pierde'}")
        
        if resultado: 
            p += apuesta
            apuesta = 1  # Si ganas, reinicias la apuesta
        else: 
            p -= apuesta
            apuesta *= 2  # Si pierdes, duplicas la apuesta
    

def dalambert(): #Monto base y si pierde aumenta en uno, si gana reduce en uno
      
      
      p = tipocapital(a)# Presupuesto inicial
      apuesta_inicial = 1
      apuesta = apuesta_inicial    # Apuesta inicial
      global XXX
      r=0
      while p >= apuesta and XXX != r:
        r +=1
        capital_money.append(p)
        resultado = jugar(apuesta)
        print(f"Presupuesto: {p}, Apuesta: {apuesta}, Resultado: {'Gana' if resultado else 'Pierde'}")
        
        if resultado: 
            p += apuesta
            apuesta = apuesta-1  # Si ganas, reinicias la apuesta
        else: 
            p -= apuesta
            apuesta = apuesta+1  # Si pierdes, duplicas la apuesta
        
        if apuesta<=0:
            apuesta = apuesta_inicial

def fibonacci():#1,1,2,3,5 el siguiente numero es la suma de los dos anteriores 
      
      
      p = tipocapital(a) # Presupuesto inicial
      apuesta = 1    # Apuesta inicial
      a1 =0 #apuesta anterior del anteior
      a2 =1 #apuesta anterior
      global XXX
      r=0
      while p >= apuesta and XXX != r:
        r +=1
        capital_money.append(p)
        resultado = jugar(apuesta)
        print(f"Presupuesto: {p}, Apuesta: {apuesta}, Resultado: {'Gana' if resultado else 'Pierde'}")
        if resultado: 
            p += apuesta
        else: 
            p -= apuesta
        sa = apuesta+a1
        a1 = apuesta
        apuesta = sa
    

def suicida(): #juego el 65% de lo que tengo, si pierdo apuesto el 100% de lo que tengo, si gano apuesto el 65% de lo que tengo
      
      
      p = tipocapital(a)# Presupuesto inicial
      apuesta = p*0.65    # Apuesta inicial
      global XXX
      r=0
      while p >= apuesta and XXX != r:
        r +=1
        capital_money.append(p)
        resultado = jugar(apuesta)
        print(f"Presupuesto: {p}, Apuesta: {apuesta}, Resultado: {'Gana' if resultado else 'Pierde'}")
        
        if resultado: 
            p += apuesta
            apuesta = p*0.65
        else: 
            p -= apuesta
            if(p!=0):
                apuesta=p
                
            
            
def strategy(l):
    global title
    if(l=="m"): title="Martingala"

    elif(l=="d"): title="Dalambert"

    elif(l=="f"): title="Fibonacci"

    elif(l=="o"): title="Suicida"

    else: title="Error"

    print(f"------------{title}------------")


    for i in range(YYY):
        if(l=="m"): martingala()

        elif(l=="d"): dalambert()

        elif(l=="f"): fibonacci()

        elif(l=="o"): suicida()


if(s in ("m", "d", "f", "o")):
    strategy(s)
    #Calculo de frecuencias relativas
    fv = chosen_colors.count('V')/len(chosen_colors)
    fr = chosen_colors.count('R')/len(chosen_colors)
    fn = chosen_colors.count('N')/len(chosen_colors)
    #----Graficar------

    fix, axs = plt.subplots(2)
    #Grafica de frecuencias


    categorias=['Rojo', 'Negro', 'Verde']
    axs[0].bar(categorias, [fr, fn, fv], color=['red', 'black', 'green'])
    axs[0].set_xlabel('Color')
    axs[0].set_ylabel('Frecuencia')
    axs[0].set_title('Frecuencia relativa')


    #Grafica de capital
    promedio = np.mean(capital_money)
    axs[1].plot(capital_money)
    axs[1].axhline(y=cfi, color='red', linestyle='-', label='Promedio')
    axs[1].set_xlabel('n (numero de tiradas)')
    axs[1].set_ylabel('cc (cantidad de capital)')
    axs[1].set_title(f"Gráfico de la estrategia {title}")
    plt.legend()
    plt.tight_layout()
    plt.show()
else: print(f"La estrategia elegida {s} no existe por favor intente nuevamente, estrategias m (martingala), d (D’Alambert), f (Fibonacci) y o (Suicida)")