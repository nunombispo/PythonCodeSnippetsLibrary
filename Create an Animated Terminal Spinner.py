import sys
import time
import itertools


def spinner(duration=5):
    spinner_cycle = itertools.cycle(['-', '\\', '|', '/'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(next(spinner_cycle))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')


# Example usage:
if __name__ == "__main__":
    print("Loading ", end="")
    spinner(5)
    print("Done!")


# Why? This snippet creates an animated spinner in the terminal using Python's standard libraries. It's a fun and
# practical way to show progress or provide visual feedback during long-running operations in CLI applications.
