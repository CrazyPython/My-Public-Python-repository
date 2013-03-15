#this program is a basic calculator
import time
import sys

print "This is a basic calculator."
time.sleep(2)
type_of_equation = raw_input("Please enter your type of equation (+,-,x,/)")
if type_of_equation == "+" :
  first_int = int(raw_input("Please enter your first integer."))
  second_int = int(raw_input("Please enter your second integer."))
  answer = first_int + second_int
  print "Your answer is ",answer
  time.sleep(5)
  sys.exit()
if type_of_equation == "-" :
  first_int = int(raw_input("Please enter your first integer."))
  second_int = int(raw_input("Please enter your second integer."))
  answer = first_int - second_int
  print "Your answer is ",answer
  time.sleep(5)
  sys.exit()
if type_of_equation == "x" :
  first_int = int(raw_input("Please enter your first integer."))
  second_int = int(raw_input("Please enter your second integer."))
  answer = first_int * second_int
  print "Your answer is ",answer
  time.sleep(5)
  sys.exit()
if type_of_equation == "/" :
  first_int = int(raw_input("Please enter your first integer."))
  second_int = int(raw_input("Please enter your second integer."))
  answer = first_int / second_int
  print "Your answer is ",answer
  time.sleep(5)
  sys.exit()
else:
  print"That is not one of the listed inputs. Please try again."
  time.sleep(3)
  sys.exit()
