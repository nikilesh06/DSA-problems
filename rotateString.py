#rotate string by given k
#for k = 2
def rotateString(s,k):
    n=len(s)
    k %= n
    return s[-k:] + s[:-k]
s="abcdefgh"
k=3
print(rotateString(s,k))