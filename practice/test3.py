import random


def sort(nums):
    box = [0]
    for i in nums:
        if i > 0:
            for ii in range(len(box)):
                ii = ii + 1
                if box[-ii] < i:
                    box.insert(len(box) - ii + 1, i)
                    break
        else:
            for ii in range(len(box)):
                ii = ii
                if box[ii] > i:
                    box.insert(ii, i)
                    break
    box.pop(0)
    return box


nums = [random.randint(-100, 1000) for _ in
        range(10)]
result = sort(nums)
print(result)
