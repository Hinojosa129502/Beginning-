#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world

wordInp = input('Input a sentence: ').split(' ')
wordOut = []
answer = ()
for item in wordInp:
    if item not in wordOut:
        wordOut.append(item)
print(' '.join(str(x) for x in sorted(wordOut)))
