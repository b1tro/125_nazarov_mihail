nums = [0,0,1,1,1,2,2,3,3,4]
for num in nums:
    if nums.count(num) > 1:
        for i in range(nums.count(num)-1):
            nums.remove(num)
print(nums)
