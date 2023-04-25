nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3

del nums1[m:len(nums1)]

for num in nums2:
    nums1.append(num)
nums1.sort()
print(nums1)
