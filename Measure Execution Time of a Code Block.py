import time


def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    return result


# Example usage
def sample_function(n):
    return sum(range(n))


measure_execution_time(sample_function, 1000000)

# Why?
# This snippet measures the execution time of a function, which is crucial for performance testing and optimization.
# It’s a practical tool for developers working on time-sensitive applications or improving code efficiency.
