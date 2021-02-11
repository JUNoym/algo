# 計算量O（n＾２）　安定　bubble Sortに類似


def gnome_sort(nums):
    len_numbers = len(nums)
    index = 0
    while index < len_numbers:
        if index == 0:
            index = index + 1

        if nums[index] >= nums[index - 1]:
            index = index + 1
        else:
            nums[index], nums[index -
                              1] = nums[index - 1], nums[index]
            index = index - 1

    return nums


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 100) for i in range(5)]
    print(gnome_sort(nums))
