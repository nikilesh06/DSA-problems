#maximum subarray(kadanes algo)
def maxSubArray(nums):
    cur =  maximum_sum = nums[0]
    for num in nums:
        cur = max(num , cur+num)
        maximum_sum = max(cur, maximum_sum)
    return maximum_sum
nums=[4,3,-2,0,0,9,8]
print(maxSubArray(nums))