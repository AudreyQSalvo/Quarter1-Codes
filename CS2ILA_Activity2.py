#Activity 2
#Use math library
import math

#Ask user for the x and y coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

#Ask user for the x and y coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

#Calculate the difference between the two points
d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

#Display the result
print("The distance between the two points is:", f"{d:.2f}")