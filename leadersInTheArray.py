def leadersInArry(nums):
    n=len(nums)
    res=[]
    max=nums[-1]
    res.append(max)
    for i in range(n-2,-1,-1):
        if max < nums[i]:
            max = nums[i]
            res.append(max)
    res.reverse()
    return res
nums=[1,17,4,3,5,2]
print(leadersInArry(nums))