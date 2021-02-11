import random
nums = [74, 54, 154, 61, 63, 2, 45, 23]


def in_order(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def Bogo(nums):
    while not in_order(nums):
        random.shuffle(nums)
    return nums


print(nums)
result = Bogo(nums)
print(nums)
