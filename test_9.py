#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
#The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.

var1, var2 = input('Enter Two Numbers: ').split(',')
var1, var2 = [int(var1), int(var2)]
arr = [[] for x in range(var1)]
j = 0
i = 0
for x in range(var2):
    for y in range(var1):
        z = i * j
        arr[y].append(z)
        j += 1
    j = 0
    i += 1
print(arr)
