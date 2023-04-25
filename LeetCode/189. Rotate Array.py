nums = [-1]
k = 3
numLength = len(nums)
if numLength!=1:
    while k > numLength:
        k-=numLength
    for i in range(numLength - k, numLength):
        nums.append(nums[i])
    for j in range(0, numLength - k):
        nums.append(nums[j])
    del nums[0:numLength]
print(nums)
