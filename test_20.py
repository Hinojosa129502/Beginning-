#A website requires the users to input username and password to register.
#Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
#Passwords that match the criteria are to be printed, each separated by a comma.
#Example
#If the following passwords are given as input to the program:
#ABd1234@1,a F1#,2w3E*,2We3345
#Then, the output of the program should be:
#ABd1234@1

passInp = input('Enter a password: ').split(',')
for x in passInp:
    if len(x) > 12:
        passInp.remove(x)
    if len(x) < 6:
        passInp.remove(x)
    if x.upper() == x:
        passInp.remove(x)
    if x.lower() == x:
        passInp.remove(x)
    if x.isalnum() == True:
        passInp.remove(x)
    if x.isdigit() == True:
        passInp.remove(x)
    if any(char.isdigit for char in x) == False:
        passInp.remove(x)
print(passInp)
