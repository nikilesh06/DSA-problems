def peakElement(arr):
    l=1
    r=len(arr)-1
    while l<r:
        mid = (l+r)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return arr[mid]
        elif arr[mid]<arr[mid-1]:
            l+=1
        else:
            r-=1
nums = [1,4,5,12,9,8,7]

print(peakElement(nums))