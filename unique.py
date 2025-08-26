#Find the Unique element in array
def is_uniqueNum(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
nums = [2,2,3,4,5,3,4]
print(is_uniqueNum(nums))