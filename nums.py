#ask user to input 3 different integers:
print("Please enter 3 whole numbers without decimals (integers)")

#as we take the input we cast it in to integers
#so we can do mathematical operations on them
num1 = int(input("Enter teh 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

#print out sum of those numbers
print(num1 + num2 + num3)

#print out the fist number minus the second number
print(num1 - num2)

#print third number multiply by the first number
print(num3 * num1)

#print sum of all numbers divided by the third number
print((num1+ num2 + num3)/ num3)