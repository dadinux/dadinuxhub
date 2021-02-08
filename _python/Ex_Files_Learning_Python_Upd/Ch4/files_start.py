#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # f = open("Mio_primo_file.txt", "w+")

  
  # Open the file for appending text to the end
  f = open("Mio_primo_file.txt", "r")

  # write some lines of data to the file
  # low = 10
  # high = 20
  # stp = 1
  # for i in range(low, high, stp):
  #   f.write("This is the line nr: " + str(i) + " of " + str(high-low) + "\r\n")
  
  # close the file when done
  # f.close()
  
  # Open the file back up and read the contents
  if f.mode == "r":
    # contents = f.read()
    fl = f.readlines()
    for x in fl:
      print(x)
    
    # print(contents)

    
if __name__ == "__main__":
  main()
