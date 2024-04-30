"""Para importar este modulo from betFunctions import funcionesAImportar"""
import random

def jugar(n): #Estrategia por color
    na = random.randint(0, 36)
    color_na = ""
    color_n = ""
    if (1 <= na <= 10) or (19 <= na <= 28):
        color_na = "R"
    elif na == 0:
        color_na = "V"
    else:
        color_na = "N"
    
    if (1 <= n <= 10) or (19 <= n <= 28):
        color_n = "R"
    elif n == 0:
        color_n = "V"
    else:
        color_n = "N"

    return color_n == color_na

  #Siempre al doble y si ganas vuelves a empezar
def martingala(): 
    print("--------Martingala--------")
    p = 100  # Presupuesto inicial
    apuesta = 1    # Apuesta inicial
    while p >= apuesta:
        resultado = jugar(apuesta)
        print(f"Presupuesto: {p}, Apuesta: {apuesta}, Resultado: {'Gana' if resultado else 'Pierde'}")
        
        if resultado: 
            p += apuesta
            apuesta = 1  # Si ganas, reinicias la apuesta
        else: 
            p -= apuesta
            apuesta *= 2  # Si pierdes, duplicas la apuesta
    

def dalambert(): #Monto base y si pierde aumenta en uno, si gana reduce en uno
      print("--------dalambert--------")
      p = 100  # Presupuesto inicial
      apuesta = 1    # Apuesta inicial
      while p >= apuesta:
        resultado = jugar(apuesta)
        print(f"Presupuesto: {p}, Apuesta: {apuesta}, Resultado: {'Gana' if resultado else 'Pierde'}")
        
        if resultado: 
            p += apuesta
            apuesta = apuesta-1  # Si ganas, reinicias la apuesta
        else: 
            p -= apuesta
            apuesta = apuesta+1  # Si pierdes, duplicas la apuesta

def fibonacci():#1,1,2,3,5 el siguiente numero es la suma de los dos anteriores 
      print("--------fibonacci--------")
      p = 100  # Presupuesto inicial
      apuesta = 1    # Apuesta inicial
      a1 =0 #apuesta anterior del anteior
      a2 =1 #apuesta anterior
      while p >= apuesta:
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
      print("--------suicida--------")
      p = 100  # Presupuesto inicial
      apuesta = p*0.65    # Apuesta inicial
      while p >= apuesta:
        resultado = jugar(apuesta)
        print(f"Presupuesto: {p}, Apuesta: {apuesta}, Resultado: {'Gana' if resultado else 'Pierde'}")
        
        if resultado: 
            p += apuesta
            apuesta = p*0.65
        else: 
            p -= apuesta
            if(p!=0):
                apuesta=p
                
            
            
martingala()

dalambert()

fibonacci()

suicida()
