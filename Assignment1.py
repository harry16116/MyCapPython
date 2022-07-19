#task 1 
import math
r = float(input(("Input the radius of the circle : " )))
print("The area of the circle with radius " , r , "is :" ,math.pi*(r**2) )

#task 2 
fileName = input("Enter the file name : ").split(".")
extension = fileName[1]
print("the extension of the file is : " , extension)