nums = [0,1,2,2,3,0,4,2]
val = 2

k = nums.count(val)
output = len(nums) - k
for i in range(k):
    nums.remove(val)
print(output)
