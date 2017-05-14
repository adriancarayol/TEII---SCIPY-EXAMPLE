import random
import time
import multiprocessing
import matplotlib.pyplot as plt
from src.algoritmos_ordenacion import Algoritmos


def process_1(lista):
    """
    Funcion para el proceso 1
    :param lista: Lista de números a ordenar
    """
    start = time.time()
    print("Empezando: %s \n" % multiprocessing.current_process().name)
    Algoritmos.minimos_sucesivos(lista)
    end = time.time()
    print(end - start)
    print("Fin: %s \n" % multiprocessing.current_process().name)
    print(lista)


def process_2(lista):
    """
    Funcion para el proceso 2
    :param lista: Lista de números a ordenar
    """
    print("Empezando: %s \n" % multiprocessing.current_process().name)
    start = time.time()
    Algoritmos.insertion_sort(lista)
    end = time.time()
    print(end - start)
    print("Fin: %s \n" % multiprocessing.current_process().name)
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

    process_jobs = []
    p1 = multiprocessing.Process(name='Minimos sucesivos', target=process_1, args=(lista,))
    process_jobs.append(p1)
    p2 = multiprocessing.Process(name='Ordenacion por seleccion (Algoritmo inestable)', target=process_2, args=(lista_2,))
    process_jobs.append(p2)

    # Iniciar procesos
    p1.start()
    p2.start()
    # Espera hasta que el proceso haya terminado su trabajo
    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
