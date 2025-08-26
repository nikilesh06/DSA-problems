def largestNum(nums):
    if not nums:
        return "Array is empty"
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
            #print(num)
    return largest
nums = list(map(int,input("enter the array: ").split()))
print(largestNum(nums))