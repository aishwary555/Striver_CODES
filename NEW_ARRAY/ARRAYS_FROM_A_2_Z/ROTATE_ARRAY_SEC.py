def rotate(nums , k):
    
    n = len(nums)
    k = k%n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums

h = 1
arr = [1, 2, 3, 4, 5]
result = rotate(arr, h)
print(result)