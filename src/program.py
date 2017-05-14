import random
import time
import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
from src.algoritmos_ordenacion import Algoritmos


def process_1(lista, q):
    """
    Funcion para el proceso 1
    :param lista: Lista de números a ordenar
    """
    start = time.time()
    print("Empezando: %s \n" % multiprocessing.current_process().name)
    Algoritmos.minimos_sucesivos(lista)
    end = time.time()
    q.put({
        'time': end - start,
        'algoritmo': 1,
    })
    print("Finalizado: %s en %f \n" % (multiprocessing.current_process().name, end - start))
    print(lista)


def process_2(lista, q):
    """
    Funcion para el proceso 2
    :param lista: Lista de números a ordenar
    """
    print("Empezando: %s \n" % multiprocessing.current_process().name)
    start = time.time()
    Algoritmos.insertion_sort(lista)
    end = time.time()
    q.put({
        'time': end - start,
        'algoritmo': 2,
    })
    print("Finalizado: %s en %f \n" % (multiprocessing.current_process().name, end - start))
    print(lista)


def process_3(lista, q):
    print("Empezando: %s \n" % multiprocessing.current_process().name)
    start = time.time()
    lista = sorted(lista)
    end = time.time()
    q.put({
        'time': end - start,
        'algoritmo': 3,
    })
    print("Finalizado: %s en %f \n" % (multiprocessing.current_process().name, end - start))
    print(lista)


def main():
    try:
        size = int(input("Introduce el tamaño de la lista: "))
    except ValueError:
        size = random.randint(1, 10000)
        print('No has introducido un número, el tamaño de la lista será de: {0}'.format(size))

    lista = []  # Para algoritmo minimos sucesivos
    for n in range(size):
        lista.append(random.randint(1, 1000))

    lista_2 = list(lista)  # Para algoritmo ordenacion por insercion
    lista_3 = list(lista)  # Para algoritmo ordenacion por insercion

    queue = multiprocessing.Queue()  # Cola para los resultados

    p1 = multiprocessing.Process(name='Minimos sucesivos', target=process_1, args=(lista, queue))

    p2 = multiprocessing.Process(name='Ordenacion por seleccion (Algoritmo inestable)', target=process_2,
                                 args=(lista_2, queue))

    p3 = multiprocessing.Process(name='Ordenacion por Timsort', target=process_3,
                                 args=(lista_3, queue))

    # Iniciar procesos
    p1.start()
    p2.start()
    p3.start()
    # Espera hasta que el proceso haya terminado su trabajo
    p1.join()
    p2.join()
    p3.join()

    times = []
    times.append(queue.get())
    times.append(queue.get())
    times.append(queue.get())
    times = sorted(times, key=lambda k: k['algoritmo'])  # Ordenamos la lista por algoritmo

    x = np.array([1, 9, 18])  # Eje x
    y = np.array([times[0]['time'], times[1]['time'], times[2]['time']])  # Eje y
    my_xticks = ['Minimos sucesivos', 'Ordenacion por seleccion', 'Ordenacion por Timsort']  # Nombres de los algoritmos
    plt.xticks(x, my_xticks)  # Asociamos nombres de algoritmos a eje x

    plt.plot(x, y)  # Creamos el grafico
    plt.xlabel('Algoritmo')  # Titulo del eje x
    plt.ylabel('Tiempo (segundos)')  # Titulo del eje y

    plt.show()  # Mostramos el grafico


if __name__ == "__main__":
    main()
