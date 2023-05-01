nums = [2,3,1,1,4]


visited = []
if len(nums) > 100:
    nums = nums[:100]
def jumper(position):
        if visited.count(position) == 0:
            visited.append(position)
            if position >= len(nums) - 1:
                jumper.result = True
                return True
            elif position < len(nums) - 1 and nums[position] != 0:
                if nums[position] > 1000:
                    jumper(position + nums[position])
                else:
                    for i in range(1, nums[position] + 1):
                            jumper(position+i)

jumper.result = False
jumper(0)
print(jumper.result)

