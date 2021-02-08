#
# Example file for working with os.path module
#
import os #os module
from os import path
import sys
import datetime
from datetime import date, time, timedelta
import time


def main():

  # Print the name of the OS
  # print(os.name + "\n\n\n")
  # print(str(os.uname()) + "\n\n\n")

# str.platform
# ===========================
# AIX               'aix'
# Linux             'linux'
# Windows           'win32'
# Windows/Cygwin    'cygwin'
# macOS             'darwin'

  if str(sys.platform) == "darwin" :
    print("\nSystem in use: MacOS\n")
  elif str(sys.platform) == "aix" :
    print("\nSystem in use: AIX\n")
  elif str(sys.platform) == "linux" :
    print("\nSystem in use: Linux\n")
  elif str(sys.platform) == "win32" :
    print("\nSystem in use: Windows\n")
  elif str(sys.platform) == "cygwin" :
    print("\nSystem in use: Windows/Cygwin\n")
  else:
    print("\nI'm not able to identify OS in use\n")


    # Check for item existence and type
    
  objname = "Mio_primo_file.txt"

  if path.exists(objname) == True and path.isfile(objname) == True:
    print("The item '" + str(objname) + "' exists and it's a file\n")               # Verifica l'esistenza del file
  elif  path.exists(objname) == True and path.isdir(objname) == True:
    print("The item '" + str(objname) + "' exists and it's a folder. \n\n")         # Verifica se l'oggetto indicato è un folder
  elif path.exists(objname) == False:
    print("The item '" + str(objname) + "' didn't exists")                          # Verifica se l'oggetto indicato esiste o meno
  

  # Work with file paths
  # print("The file path is: " + str(path.realpath("Mio_primo_file.txt")))
  # print("The file name and path are: " + str(path.split(path.realpath("Mio_primo_file.txt"))))

  # Get the modification time
  # t = time.ctime(path.getmtime("Mio_primo_file.txt"))
  # print(t)
  # t2 = datetime.datetime.fromtimestamp(path.getmtime("Mio_primo_file.txt"))
  # print(t2)

  
  # Calculate how long ago the item was modified
  # td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("Mio_primo_file.txt"))
  # print("It has been " + str(td) + " since the file was modified")
  # print("Or, " + str(td.total_seconds()) + " seconds")
  
  
if __name__ == "__main__":
  main()
