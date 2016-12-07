# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:

input_number = input('Input a number: ')
x = input_number #4
add_list = []
y = input_number
while x > 2:
    y = y * (x-1) #12
    x -= 1
print y
