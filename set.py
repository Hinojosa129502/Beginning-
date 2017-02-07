
listInp = input('enter a list of numbers: ').split(',')
listOut = []
s = set()
for x in listInp:
    if x in s:
        listOut.append(x)
    s.add(x)
print(listOut)
