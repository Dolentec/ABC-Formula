##########################################################################
# Author        : Niels van Rheenen
# Goal          : This Program can find the roots of a quadratic formula
# Date / version : v0.1.1
#
# Input          : A, B and C
# Output         : X1 and X2
# Used Calculations / algorithms :
#
# Imported Python modules: System,Operating system and Time
# Other Notes : -
#
##########################################################################


import sys, os
import time
# importing modules

os.system('cls')
# To clear the console so it looks nicer.

print("---------------------------------------------------------------")
print("This is a script to calculate x in a second degree formula like,")
print("ax^2 + bx + c = 0")
print("---------------------------------------------------------------")
# Printing yhe explanation of the script.
time.sleep(4)



A = input("what is your number for A? ")
# Input for A.

while int(A) == 0:
    print("A can't be zero.")
    A = input("what is your number for A? ")
# While A is 0 the code doesn't progress


B = input("What is your number for B? ")
C = input("What is your number for C? ")htdf
# input for B and C


D = (int(B) ** 2) - (4 * int(A) * int(C))
# Calculate the discriminant.

print("The Discriminant is " + str(D))
# Printing the discriminant.


x1 = (-int(B) - (int(D)**(.5))) / (2 * int(A))
# Calculating Root1.

x2 = (-int(B) + (int(D)**(.5))) / (2 * int(A))
# Calculating Root2.
os.system('cls')

print("---------------------------------------------------------------")
print("The results,")
if D < 0:
    print("There are no solutions")
elif D > 0:
    print("There are two solutions,")
    print(str(x1))
    print(str(x2))
elif D == 0:
    print("There is one solution,")
    print(str(x1))
print("---------------------------------------------------------------")
# printing the results based on the value of the discriminant.