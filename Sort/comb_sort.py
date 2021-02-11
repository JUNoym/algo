# ポイント　SwapがFalseになるまで並び替える
# つまりGapを1.3で割って１になるまでSwapし続けて、交換が行われなくなるまで続ける
# 計算量　O（n^2/2**g）安定はしていない


def comb_sort(numbers):
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False  # SwappedがTrueにならなかったらwhile文を抜けるようになる

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]
                swapped = True

    return numbers


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(nums)
    result = comb_sort(nums)
    print(result)
