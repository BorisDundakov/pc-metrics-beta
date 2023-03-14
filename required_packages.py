# attempting to get data from PC
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install('psutil')
install('h2o_wave')
