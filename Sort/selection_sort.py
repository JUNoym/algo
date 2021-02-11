# 計算量　O（n＾２）bubble Sortの改良　安定している

def selection_sort(numbers):
    let_numbers = len(numbers)
    for i in range(let_numbers):
        min_idx = i
        for j in range(i + 1, let_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(selection_sort(nums))
