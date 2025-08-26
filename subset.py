#check if one array is a subset of another 
def is_subset(arr1,arr2):
    set1= set(arr1)
    for i in arr2:
        if i not in set1:
            return False
    return True
num1=[1,2,3,4,5,6]
num2=[2,4,7]
print(is_subset(num1,num2)) 