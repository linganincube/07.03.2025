import psutil
import time
import datetime
import csv
import os

# --- Configuration ---
LOG_INTERVAL_SECONDS = 5  # How often to log data (in seconds)
LOG_FILE = "system_performance_log.csv"
# -------------------

def get_system_stats():
    """Retrieves current CPU and Memory usage."""
    cpu_usage = psutil.cpu_percent(interval=1) # Get CPU usage over 1 second
    memory_info = psutil.virtual_memory()
    memory_usage_percent = memory_info.percent # Total memory usage percentage
    return cpu_usage, memory_usage_percent

def log_stats(timestamp, cpu, memory, file_path):
    """Logs the stats to a CSV file."""
    file_exists = os.path.isfile(file_path)
    is_empty = os.path.getsize(file_path) == 0 if file_exists else True

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['Timestamp', 'CPU Usage (%)', 'Memory Usage (%)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only if file is new or empty
        if not file_exists or is_empty:
            writer.writeheader()

        writer.writerow({'Timestamp': timestamp,
                         'CPU Usage (%)': cpu,
                         'Memory Usage (%)': memory})

def monitor_system(log_file, interval):
    """Main monitoring loop."""
    print(f"Starting system monitoring. Logging to '{log_file}' every {interval} seconds.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            # Get current timestamp
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Get stats
            cpu, memory = get_system_stats()

            # Log stats
            log_stats(now, cpu, memory, log_file)

            # Wait for the next interval
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    monitor_system(LOG_FILE, LOG_INTERVAL_SECONDS)