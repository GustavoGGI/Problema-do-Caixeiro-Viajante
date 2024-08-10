import time
import psutil

def measure_performance(func):
    """
    Mede o tempo de execução e o uso de memória de uma função.

    :param func: Função a ser medida
    :return: Resultado da função, tempo de execução em segundos e uso de memória em MB
    """
    start_time = time.time()  
    start_memory = psutil.Process().memory_info().rss / 1024 ** 2  # Memória inicial em MB
    result = func()
    end_time = time.time()
    end_memory = psutil.Process().memory_info().rss / 1024 ** 2  # Memória final em MB
    time_taken = end_time - start_time
    memory_used = end_memory - start_memory
    return result, time_taken, memory_used
