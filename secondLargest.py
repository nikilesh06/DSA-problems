def secondLargest(nums):
    largest = 0 
    second = 0
    if len(nums) < 2:
        return "List must have more than 2 elements"
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num < largest:
            second = num
    return second
nums=[10,20,50,100,90,8,98,99]
print(secondLargest(nums))