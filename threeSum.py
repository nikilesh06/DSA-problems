def threeSum(nums,target):
    nums.sort()
    for i in range(len(nums)):
        l=1
        r=len(nums)-1
        while l<r:
            total = nums[i]+nums[l]+nums[r]
            if total == target:
                return True
                
            elif total > target:
                r-=1
            else:
                l+=1
    return False
nums=[1,8,10,9,6,5]
target =27
print(threeSum(nums,target))
