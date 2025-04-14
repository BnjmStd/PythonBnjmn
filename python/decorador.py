"""
    -
"""

import time

def measure_time(func):
    """
        -
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start} seconds")
    return wrapper

def gretting(func):
    """
        -
    """
    def wrapper(*args, **kwargs):
        print('Hello,')
        func()
    return wrapper

@gretting
@measure_time
def morning(name):
    """
        -
    """
    print(f"Good Morning, {name}")

morning('John')