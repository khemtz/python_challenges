#! /usr/bin/python3 
import math

str_input = input("Bring 3 Integer Numbers (separate by space):")
n = str_input.split(" ") + str_input.split(" ")
if (len(n) == 6):
   values = [True if float(n[i]) == math.sqrt((float(n[i+1]) * float(n[i+1])) + (float(n[i+2]) * float(n[i+2]))) else False for i in range(3)]
   try:
      i=values.index(True)
      print ("These numbers are a valid pythagorean triplet when:\n  A (side)=" + str(int(n[i+1])) + "\n  B (side)=" + str(int(n[i+2])) + "\n  C (hypotenuse)=" + str(int(n[i])))
   except ValueError: print ("These numbers are not a valid pythagorean triplet")
else: print ("Input Error, please write 3 numbers separated by space, for example: \"3 5 4\"")
