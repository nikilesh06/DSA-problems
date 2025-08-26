def twoSum(nums,target):
    for ind1 in range(len(nums)):
        for ind2 in range(ind1+1,len(nums)):
            if nums[ind1] + nums[ind2] == target:
                return [ind1,ind2]
    return False
nums=[2,5,6,10]
target = 13
print(twoSum(nums,target))