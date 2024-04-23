import random
import math

class GenerarAleatorios:

    @staticmethod
    def generar_random():
        return round(random.uniform(0,1),6)
    
    @staticmethod
    def uniforme(int1, int2, muestra):   
        serie_out = [] #inicializamos la serie de salida con un array vacio
        for i in range(muestra): #itera segun el tamaño de muestra  
            rnd = GenerarAleatorios.generar_random() #genera un numero random entre 0 y 1
            numero = int1 + rnd*(int2 - int1) #genera el numero aleatorio uniforme
            serie_out.append(numero) #lo añade a la lista
        return serie_out
    
    @staticmethod
    def exponencial(lambd, media, muestra):
        serie_out = [] #inicializamos la serie de salida con un array vacio
        for i in range(muestra):
            rnd = GenerarAleatorios.generar_random() #genera un numero random entre 0 y 1
            numero = (-1/lambd)*(math.log(1-rnd)) #genera el numero aleatorio 
            serie_out.append(numero) #lo añade a la lista
        return serie_out
    
    @staticmethod
    def normal(media, desviacion, muestra):
        serie_out = []
        for i in range(muestra):
            rnd1 = GenerarAleatorios.generar_random() #genera un numero random entre 0 y 1
            rnd2 = GenerarAleatorios.generar_random() #genera un numero random entre 0 y 1
            if rnd1 == 0: rnd1 = 0.0000001
            if rnd2 == 0: rnd1 = 0.0000001
            numero1 = (math.sqrt(-2*(math.log(rnd1)))*math.cos(2*math.pi*rnd2))*desviacion + media #genera el numero aleatorio
            serie_out.append(numero1)
            numero2 = (math.sqrt(-2*(math.log(rnd1)))*math.sin(2*math.pi*rnd2))*desviacion + media
            serie_out.append(numero2)
        return serie_out