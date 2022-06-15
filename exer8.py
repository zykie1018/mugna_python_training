import time


def timing_decorator(func):
    def wrapper(x, y):
        start_time = time.perf_counter()
        result = func(x, y)
        end_time = time.perf_counter()
        time_diff = end_time - start_time
        execution_time = time_diff * 1000 # convert to milliseconds
        print(f"Time executed: {execution_time:.5f} milliseconds")
        return result
    return wrapper

@timing_decorator
def addition_func(x, y):
    print(f"Sum is: {x+y}")
    # print(f"Time it took: {}")

addition_func(4, 5)