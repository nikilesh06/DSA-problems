def largestDigit(num):
    count = [0] * 10
    for i in num:
        count[i]+=1
    result =[]
    for j in range(9,-1,-1):
        result.extend([j] * count[j])
    return int("".join(map(str,result)))
num = [3,4,7,8,9,1,2,2]
print(largestDigit(num))