#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3


wordInp = input('Input a sentence: ')
cnt = 0
for x in wordInp:
    if x.isdigit() == True:
        cnt += 1
print('LETTERS', len(wordInp) - wordInp.count(' '))
print('DIGITS', cnt)
