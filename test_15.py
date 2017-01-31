#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3


wordInp = input('Input a sentence: ')
numCt = 0
alpCt = 0
for x in wordInp:
    if x.isdigit() == True:
        numCt += 1
    if x.isalpha() == True:
        alpCt += 1
print('DIGITS', numCt)
print('LETTERS', alpCt)
