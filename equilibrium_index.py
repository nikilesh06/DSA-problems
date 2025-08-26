def equilibriumIndex(nums):
    totalSum = sum(nums)
    leftSum=0
    for i in range(len(nums)):
        totalSum -= nums[i]
        if totalSum == leftSum:
            return nums[i]
        leftSum += nums[i]
    return -1
nums = [1,5,8,2,3,1]
print(equilibriumIndex(nums))
    