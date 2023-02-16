import time
import os

def monitor_file(file_path):
    previous_data = ''
    while True:
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the data from the file
            with open(file_path, 'r') as f:
                data = f.read()
            # Compare the current data with the previous data
            if data != previous_data:
                print(f"File '{file_path}' has been updated.")
                previous_data = data
        else:
            print(f"File '{file_path}' does not exist.")
        time.sleep(1)

# Example usage
file_path = r'C:\example\data.txt'
monitor_file(file_path)
print "why"