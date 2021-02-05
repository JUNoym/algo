# 適当に並び替える猿でもできるソート めちゃくちゃ時間がかかる
import random


def in_order(numbers):
    # リストのインデックス番号を取得したい
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


def bogo_sort(numbers):
    while not in_order(numbers):  # 順序通りに並んでいない場合は順序通りになるまでシャッフルする
        random.shuffle(numbers)  # これはNONEを返すので
    return numbers


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(bogo_sort(nums))
# test
