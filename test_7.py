#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class Strn():
    def __init__(self):
        self.s = ""
    def getStr(self):
        self.s = input('Enter a String: ')
    def UpStr(self):
        print(self.s.upper())
StrObj = Strn()
print(StrObj.getStr())
print(StrObj.UpStr())
