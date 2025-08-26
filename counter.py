from collections import Counter
 
s=[1,2,1,1,2,3,4,5,6]
# s="aabcccdd"
freq = Counter(s)
for char in s:
    print(char ,"=",freq[char])