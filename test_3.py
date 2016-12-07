# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

div = 7
mult = 5
ran = range(2000,3500)
for x in ran:
    if x % 7 == 0 and x % 5 != 0:
        print x
