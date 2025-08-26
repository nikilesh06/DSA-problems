def fourSum(nums,target):
    nums.sort()
    n=len(nums)
    result = []
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and nums[j] ==nums[j-1]:
                continue
            l=j+1
            r=n-1
            while l<r:
                total = nums[i]+nums[j]+nums[l]+nums[r]
                if total == target:
                    result.append([nums[i],nums[j],nums[l],nums[r]])
                    while l<r:
                        if nums[l]==nums[l+1]:
                            l+=1
                        elif nums[r] == nums[r-1]:
                            r-=1
                    l+=1
                    r-=1
                elif total<target:
                    l+=1
                else:
                    r-=1
    return result
nums=[1,5,3,10,4,6,7,9]
print(fourSum(nums,24))
                    