# -*- coding: utf-8 -*-

import math
print "\t\t***********************************************************************"
print "\t\t*                                                                     *"
print "\t\t*  Welcome to the North Lake Senior Campus math Python DoDaki thing   *"
print "\t\t* You need to make choices by enterng the appropriate number for each *"
print "\t\t*                                                                     *"
print "\t\t***********************************************************************"

print "1: Circle"
print "2: Triangle"
print "3: Parallelogram"
print "4: Trapezium"
print "5: Prism"
print "6: Pyramid"
print "7: Cylinder"
print "8: Cone"
print "9: Sphere\n"

choice=raw_input( "Choose the mathematical formula you want to practice...")

if choice=="1": # Circle stuff
 print "\n1: Area"
 print "2: Diameter"
 print "3: radius \n"

 circlechoice=raw_input("Choose between the Area, Diameter or Radius of a Circle...")
 if circlechoice=="1":
    counter="0"
    while True:
      AreaFormula=raw_input( "\nWhat is the formula for the area of a circle? A = ...")
      if AreaFormula in ("3.1415xR^2","piR**2","piR^2","pir^2","3.1415xR**2","3.1415R**2","πr**2","πr^2","πR**2","πR^2","math.pi(r**2) \n"):
         print "\nExcellent \n"
         counter="1"
         print "Now lets try your formula ",AreaFormula,". In Python the preffered way is \"math.pi(r**2)\"\n"
         r=float(raw_input("Enter a radius for a circle... "))
         youranswer=float(raw_input("\nBefore we show you our answer, what do you think the answer is?  Rounded to 4 decimal places... "))
#         print "your answer is",youranswer
         actualanswer=float(math.pi*(r**2))
         actualanswer=("%.4f" % actualanswer)
#         print "The actual answer is ", actualanswer
         if float(youranswer) == float(actualanswer):
            print "\nAwesome, you got the right answer"
         else:
            print "\nOh dear how sad"
      else:
         print "Woops, try again"
      if counter=="1": break 
 elif circlechoice=="2":
    counter="0"
    while True:
      AreaFormula=raw_input( "\nWhat is the formula for the Diameter of a circle? D = .....? ")
      if AreaFormula in ("2piR","2x3.1415xR","2πR","piD"):
         print "Excellent"
         counter="1"
      else:
         print "Woops, try again"
      if counter=="1": break 
    print "You have chosen to work with the Diameter of a Circle"
    print "C = 2πr = πD, where C is the circumference"
 elif circlechoice=="3":
    print "You have chosen to work with the Radius of a Circle"
    print "r is the radius and D is thediameter"
 else:
    print "Well that is not a good choce"
elif choice=="2":
 print "Triangle"
elif choice=="3":
 print "Paralleogram"
elif choice=="4":
 print "Trapezium"
elif choice=="5":
 print "Prism"
elif choice=="6":
 print "Pyramid"
elif choice=="7":
 print "Cylinder"
elif choice=="8":
 print "Cone"
elif choice=="9":
 print "Sphere"
else:
 print "Well that choice just sucked!"

