#Write a program that computes the net amount of a bank account based a transaction log from console input.
#The transaction log format is shown as following:
#D 100
#W 200
#¡­
#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:
#D 300
#D 300
#W 200
#D 100
#Then, the output should be:
#500

bal = 0
while True:
    transLog = input('D/W Amount: ').split()
    if transLog[0] != 'i':
        if transLog[0] == 'D':
            bal += int(transLog[1])
        if transLog[0] == 'W':
            bal -= int(transLog[1])
    else:
        break;
print(bal)
