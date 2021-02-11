nums = [74, 54, 154, 61, 63, 2, 45, 23]


def Bubble_sort(nums):
    len_numbers = len(nums)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


result = Bubble_sort(nums)
print(nums)
