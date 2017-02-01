#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program:
#9
#Then, the output should be:
#11106

numInp = input('Enter a number: ')
numInp = int(numInp)
numTrc = numInp
count = 0
for x in range(4):
    count += numInp
    numInp = (numInp * 10) + numTrc
print(count)
