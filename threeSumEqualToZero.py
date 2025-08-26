#return sum three of numbers tht equal to zero
def threeSumZero(nums):
    nums.sort()
    triplet=[]
    for i in range(len(nums)):
        if i!=0 and nums[i] == nums[i-1]:
            continue
        l=1
        r=len(nums)-1
        while l<r:
            total = nums[i]+nums[l]+nums[r]
            if total > 0:
                r-=1
            elif total < 0:
                l+=1
            else:
                triplet.append([nums[i],nums[l],nums[r]])
                l+=1
                while l<r:
                    if nums[l] == nums[l-1]:
                        l+=1

    return triplet           
nums=[-1,-1,2,-3,5,12]
print(threeSumZero(nums))