# File Cleaner Script

This simple Python script helps you clean up files in a specified folder that have been created more than a certain threshold time ago. It can be used to automatically remove old files from a directory.

## Prerequisites

1. Python (>= 3.6) should be installed on your system.

## Usage

1. Download the `deletingFiles.py` script to your desired location.

2. Open the script in a text editor and set the `folder_path` variable to the path of the folder you want to clean.

3. Set the `threshold` variable to the desired time limit in seconds. By default, it is set to 30 minutes (30 * 60 seconds).

4. Save the changes to the script.

5. You can manually run the script by executing it:

   ```bash
   python deletingFiles.py
## Running as a Cron Job

To automate the process and run the script as a cron job, follow these steps:

1. Open your terminal and edit your crontab file:

   ```bash
   crontab -e
2. Add a new line to schedule the script. The following is an example of running the script every 30 minutes:

   ```bash
   */30 * * * * /usr/bin/python3 /path/to/deletingFiles.py
   ```
   Replace `/usr/bin/python3` with the path to your Python interpreter (you can find it using which python3) and `/path/to/clean_files.py` with the actual path to the script. Save and exit the crontab editor.

3. Now, your script will run automatically at the specified schedule, cleaning up old files in the specified folder.   
