def pseudoBinary(num):
    maxBinary = 0
    while num>0:
        digit = num%10
        maxBinary = max(digit,maxBinary)
        num = num//10
    return maxBinary
num = 91
print(pseudoBinary(num))