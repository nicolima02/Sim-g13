from generador import GenerarAleatorios
from grafico import GenerarGrafico

def main():
    opcion = -1
    # Mostrar menu de distribuciones
    while opcion != 0:
        print("\n1) Distribucion uniforme \n2) Distribucion exponencial negativa\n3) Distribucion normal \n0) Salir")
        opcion = int(input("Eleccion: "))

        if opcion not in [1, 2, 3, 0]:
            print("No es una opcion valida")
            continue
        elif opcion == 0:
            break
        else:
            muestra = int(input("Seleccione el tamaño de la muestra: "))
            if opcion == 1:
                #intervalos a y b
                int1 = float(input("Ingrese el valor de 'a' para la distribución uniforme: "))
                int2 = float(input("Ingrese el valor de 'b' para la distribución uniforme: "))
                #Llamar a funcion de generacion de numeros aleatorios
                serie = GenerarAleatorios.uniforme(int1, int2, muestra)
            elif opcion == 2:
                #Ingresa parametros de la distribucion exponencial negativa
                periodo = float(input("Ingrese el valor del periodo en el que ocurren los eventos: ")) #periodo en el que ocurren los eventos
                evento = float(input("Ingrese la cantidad de eventos que ocurren en el periodo: ")) #cantidad de veces que ocurre el evento
                lambd = evento/periodo #calculo de lambda
                media = float(input("Ingrese la media con la que ocurre el evento: "))
                serie = GenerarAleatorios.exponencial(lambd, media, muestra)
            elif opcion == 3:
                #ingresa parametros media y desviacion
                media = float(input("Ingrese el valor de la media: ")) #periodo en el que ocurren los eventos
                desviacion = float(input("Ingrese el valor de la desviacion: ")) #cantidad de veces que ocurre el evento
                serie = GenerarAleatorios.normal(media, desviacion, muestra)

            intervalos = int(input("Ingrese el número de intervalos (5, 10 o 15): "))
            
            frecuencias, bins = GenerarGrafico.generar_histograma(serie, intervalos) #Toma como entrada una secuencia de datos y opcionalmente el número de bins en los que se dividirá 
            #el rango de valores. Devuelve dos arrays: el primero contiene las frecuencias de los valores en cada bin, y el segundo contiene los límites de los bins.
            GenerarGrafico.mostrar_tabla_frecuencias(frecuencias, bins) #agrupa los intervalos y las frecuencias
            GenerarGrafico.visualizar_histograma(frecuencias, bins) #abre el grafico
            
if __name__ == "__main__":
    main()