import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from src.multithreading import Producer, Consumer
from queue import Queue


def main():
    queue = Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()


if __name__ == "__main__":
    main()
