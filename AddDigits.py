#given an integer num,repeatedly add all its digits until the result has only 1 digit,Return that one digit 
def addDigit(num):
    if num == 0:
        return 0
    if num  % 9 == 0:
        return 9
    return num%9
num = 18
print(addDigit(num))