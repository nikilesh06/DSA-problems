def binarySearch(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        middle_ind = (l+r)//2
        middle = nums[middle_ind]
        if middle > target:
            r=middle_ind-1
        elif middle < target:
            l=middle_ind+1
        else:
            return middle_ind
    return -1
nums=[0,4,7,9,10,12,56]
print(binarySearch(nums,8))
        