def countVowelAndConsonant(text):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    vowelCount=0
    consonantCount = 0
    for i in text:
        if i.isalpha():
            if i in vowels:
                vowelCount+=1
            else:
                consonantCount+=1
    return [vowelCount,consonantCount]
string = 'A string iss defined'
print(countVowelAndConsonant(string))