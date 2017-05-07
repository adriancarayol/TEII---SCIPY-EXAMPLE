from threading import Thread
import time
import random


class Producer(Thread):
    def __init__(self, queue):
        """
        Inicializador de la clase Producer
        :param queue: 
        """
        Thread.__init__(self)  # Llamada al constructor de Thread
        self.queue = queue

    def run(self):
        """
        Override metodo run
        """
        for i in range(1000):
            item = random.randint(0, 1024)
            self.queue.put(item)  # Introducimos el item generado en la cola
            print('Producer %s genera: %d' % (self.name, item))
            time.sleep(0.2)  # Productor espera 1 segundo


class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer %s get: %d' % (self.name, item))
            self.queue.task_done()
