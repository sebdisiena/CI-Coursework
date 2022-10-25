# import numpy library to perform product function
import numpy

# input number from user
userInput = int(input("enter you number: "))

# increase user input number by 1 to obtain a rage including user input
Input = userInput + 1 

# generate the list of numbers in the range
userInputList = list(range(Input))

# remove the 0 element
userInputList = [i for i in userInputList if i !=0]

# perform product function
userFactorial = numpy.prod(userInputList)

# display result
print("The factorial of " + str(userInput) + " is: " + str(userFactorial))