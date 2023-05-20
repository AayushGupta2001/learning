# Python program to find
# sum of two numbers

# Reading two numbers
number1 = input('Enter first number: ')
number2 = input('Enter second number: ')

# Converting to float
# Conversion is required because
# input() function return string
number1 = float(number1)
number2 = float(number2)

# Addition
result = number1 + number2

# Displaying result
print('Sum of %0.2f and %0.2f is %0.2f' % (number1, number2, result))
