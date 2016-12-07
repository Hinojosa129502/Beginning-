#With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
#such that is an integral number between 1 and n (both included). and then the program should print
#the dictionary.

end_number = input("Input a number: ")
n = end_number
number_dict = {}
ran = range(1,n)
x = 1
for x in ran:
    while x < (n+1):
        number_dict[x] = x*x
        x += 1
print number_dict
