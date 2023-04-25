nums = [2,2,1,1,1,2,2]
nums.sort()
maxc = 0
output = 0
for num in nums:
    if nums.count(num) > maxc:
        maxc = nums.count(num)
        output = num
    del nums[nums.index(num):nums.index(num)+nums.count(num)-1]
print(nums, output)