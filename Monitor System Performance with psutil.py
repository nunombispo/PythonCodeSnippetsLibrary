# pip install psutil

import psutil


def monitor_system(interval=1):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=interval)
            memory = psutil.virtual_memory()
            print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory.percent}%")
    except KeyboardInterrupt:
        print("Monitoring stopped.")


if __name__ == "__main__":
    monitor_system()


# Why? This snippet leverages the psutil library to continuously monitor your system's CPU and memory usage in
# real-time. It's perfect for quick performance checks, debugging resource-intensive applications, or integrating
# lightweight monitoring into your scripts.
