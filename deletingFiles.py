import os
import time

folder_path = '/path/to/filesContainer'

current_time = time.time()
threshold = 30 * 60  # threshold in seconds [1/2 hour here]

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    creation_time = os.path.getctime(file_path)
    
    if (current_time - creation_time) > threshold:
        os.remove(file_path)
