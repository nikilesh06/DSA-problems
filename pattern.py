def pattern(n):
    for i in range(1,n+1):
        temp=i
        for j in range(1,i+1):
            print(temp,end=" ")
            temp += n-j
        print()
n=int(input("Enter the number: "))
print(pattern(n))