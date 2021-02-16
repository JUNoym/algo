# Pivot と　jを比べて　Pivotが大きい場合 i += 1, Swap (list[i], list[j])をする
# これをしていくとPivotより小さい数字は前に行き、Pivotより大きい数字はどんどん後ろに行く

def partition(numbers, low, high):
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):  # lowはもともと０が入っている
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1


def quick_sort(numbers):
    def _quick_sort(numbers, low, high):
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(numbers, partition_index+1, high)

    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


if __name__ == "__main__":
    nums = [1, 8, 3, 9, 4, 5, 7]
    print(quick_sort(nums))
