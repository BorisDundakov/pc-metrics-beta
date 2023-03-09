# attempting to get data from PC
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install('psutil')

import psutil, speedtest

cpu_percentage = psutil.cpu_percent()
virtual_memory_percentage = psutil.virtual_memory().percent
available_memory_percentage = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

print("Your CPU usage is: ", f"{cpu_percentage:.1f}", "%")
print("Your Available memory is: ", f"{available_memory_percentage:.1f}", "%")
print("Your virtual memory percentage is: ", f"{virtual_memory_percentage:.1f}", "%")

speed_test = speedtest.Speedtest()


def bytes_to_mb(bytes):
    KB = 1024  # One Kilobyte is 1024 bytes
    MB = KB * 1024  # One MB is 1024 KB
    return int(bytes / MB)


download_speed = bytes_to_mb(speed_test.download())
print("Your Download speed is", download_speed, "MB")

upload_speed = bytes_to_mb(speed_test.upload())
print("Your Upload speed is", upload_speed, "MB")
