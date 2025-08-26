from collections import Counter
def odd_count_chars(s):
    freq = Counter(s)
    result=""
    for char in s:
        if freq[char] % 2 and char not in result:
            result += char
    return result
s="aabbccdc"
print(odd_count_chars(s))
    