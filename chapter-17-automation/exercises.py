# Chapter 17 - Exercise Solutions
import schedule
import time

# 1. Automated daily report
def generate_daily_report():
    """Generate a summary report from a CSV file."""
    import csv
    from datetime import datetime
    
    print(f"[{datetime.now()}] Generating report...")
    # In production, this would read real data
    print("  Report generated and saved.")

# schedule.every().day.at("09:00").do(generate_daily_report)

# 2. File watcher
import os

def watch_folder(folder, interval=5):
    """Watch a folder for new files."""
    known_files = set(os.listdir(folder))
    print(f"Watching {folder}...")
    while True:
        current = set(os.listdir(folder))
        new_files = current - known_files
        if new_files:
            for f in new_files:
                print(f"  New file: {f}")
                # Process new file here
        known_files = current
        time.sleep(interval)

# 3. Retry decorator
import functools

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Attempt {attempt+1} failed: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (2 ** attempt))
            raise Exception(f"Failed after {max_attempts} attempts")
        return wrapper
    return decorator
