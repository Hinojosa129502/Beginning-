#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

wordInp = input('Enter a sentence: ')
letUp = 0
letLow = 0
for x in wordInp:
    if x.isupper() == True:
        letUp += 1
    if x.islower() == True:
        letLow += 1
print('UPPER', letUp)
print('LOWER', letLow)
