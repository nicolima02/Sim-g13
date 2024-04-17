import numpy as np
import matplotlib.pyplot as plt

class GenerarGrafico:

    @staticmethod
    def generar_histograma(serie, intervalos):
        frecuencias, bins = np.histogram(serie, bins=intervalos)
        return frecuencias, bins

    @staticmethod
    def visualizar_histograma(frecuencias, bins):
        plt.bar(bins[:-1], frecuencias, width=np.diff(bins), align="edge", color='skyblue', edgecolor='black') #np.diff toma la diferencia entre el elemento de un array con su vecino
        #se le extrae el ultimo elemento para que sean n barras
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')
        plt.title('Histograma de frecuencias')
        plt.show()

    @staticmethod
    def mostrar_tabla_frecuencias(frecuencias, bins):
        print("_________________________________________________________________")
        print("\033[1mIntervalo\t\tFrecuencia\033[0m")
        for i in range(len(frecuencias)):
            print(f"\033[91m{bins[i]:.4f}-{bins[i+1]:.4f}\033[0m\t\t\033[92m{frecuencias[i]}\033[0m") #:.4f redondea en 4 decimales
        print("_________________________________________________________________")