#Write a program, which will find all such numbers between 1000 and 3000 (both included)
#such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.

numList = []
for x in range(1000,3001):
    if x % 2 == 0:
        numList.append(x)
print(','.join(str(s) for s in numList))
