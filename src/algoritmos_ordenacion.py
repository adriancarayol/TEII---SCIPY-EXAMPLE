class Algoritmos(object):
    """
    Clase que contiene los siguientes algoritmos de ordenacion
        - Ordenamiento por seleccion
        - Ordenamiento por insercion
    """

    @staticmethod
    def minimos_sucesivos(lista):
        """
        Ordena una lista de números
        por el algoritmo minimos sucesivos.
        Ordenamiento por selección (Selection Sort en inglés).
        :param lista: Lista con los números a ordenar
        """
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if lista[i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    @staticmethod
    def insertion_sort(lista):
        """
        Ordena una lista de números
        por el algoritmo ordenamiento por inserción
        (InsertionSort en inglés)
        :param lista: Lista con los números a ordenar
        """
        for i in range(1, len(lista) - 1):
            Algoritmos.__inserta(lista, i + 1, lista[i + 1])

    @staticmethod
    def __inserta(lista, k, v):
        """
        Metodo auxiliar para el algoritmo de ordenacion
        insertion_osrt
        :param lista: Lista con los números a ordenar
        :param k: Posición del siguiente elemento de la lista
        :param v: Siguiente elemento de la lista
        """
        for i in range(k):
            if lista[i] > v:
                lista.pop(k)
                lista.insert(i, v)
                return
