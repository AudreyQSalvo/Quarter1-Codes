#Code 1
#Declare three variables and ask user to enter one floating-point number in each variable
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

#Add the three numbers and store the result in a new floating-point variable
sum = num1 + num2 + num3

#Display the value of sum to the user with appropriate formatting
print(" ")
print("The total of the three numbers is:", f"{sum:.2f}")