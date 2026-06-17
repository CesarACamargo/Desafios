from utils_log import log_decorator
from timer import time_measure_decorator

@log_decorator
@time_measure_decorator
def soma(a, b):
    return a + b

soma(2,3)
soma(3,7)

