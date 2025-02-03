import concurrent.futures
import time


def task(n):
    time.sleep(1)
    return f"Task {n} done"


def run_in_parallel():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(task, range(5))
    return list(results)


# Example usage
start = time.perf_counter()
print(run_in_parallel())
# Output: ['Task 0 done', 'Task 1 done', 'Task 2 done', 'Task 3 done', 'Task 4 done']
end = time.perf_counter()
print(f"Executed in {end - start:.2f} seconds")  # Around 1 second instead of 5!


# Why?
# This snippet runs multiple tasks in parallel using ThreadPoolExecutor, making it perfect for I/O-bound operations
#     like API calls, file processing, and web scraping.
