# 挿入ソート　計算量O(n^2) 安定
# 見る値を適切な位置まで持っていく

def insertion_sort(nums):
    len_numbers = len(nums)
    for i in range(1, len_numbers):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = tmp

    return nums


if __name__ == '__main__':
    nums = [1, 7, 3, 2, 8, 5]
    print(insertion_sort(nums))
