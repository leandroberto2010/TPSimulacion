"""Para importar este modulo from betFunctions import funcionesAImportar"""
import random

def jugar(n):
    na = random.randint(0, 36)
    if n == na:
        return True
    else:
        return False

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
