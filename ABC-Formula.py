import sys, os
import time

os.system('cls')
#To clear the console so it looks nicer.

print("---------------------------------------------------------------")
print("This is a script to calculate x in a second degree formula like,")
print("ax^2 + bx + c = 0")
print("---------------------------------------------------------------")
time.sleep(4)



A = input("what is your number for A? ")

while int(A) == 0:
    print("A can't be zero.")
    A = input("what is your number for A? ")


B = input("What is your number for B? ")
C = input("What is your number for C? ")


D = (int(B) ** 2) - (4 * int(A) * int(C))

print("D is " + str(D))

x1 = (-int(B) - (int(D)**(.5))) / (2 * int(A))

x2 = (-int(B) + (int(D)**(.5))) / (2 * int(A))

os.system('cls')

print("---------------------------------------------------------------")
print("The results,")
if D < 0:
    print("Er zijn geen oplossingen")
elif D > 0:
    print("er zijn twee oplossingen, namelijk")
    print(str(x1))
    print(str(x2))
elif D == 0:
    print("er is een oplossing, namelijk")
    print(str(x1))


print("---------------------------------------------------------------")