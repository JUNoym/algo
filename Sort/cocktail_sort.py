# シェーカーソート　バブルソートの改良
# バブルソートのように最後までやらなくても、SWAPがFalseのまま終われば終了できるという点で
# バブルソートよりも早い場合がある
#  計算量　O（n^2）


def cocktail_sort(numbers):
    len_numbers = len(numbers)
    swapped = True
    start = 0  # 調べ始める最初のインデックス番号を取得
    end = len_numbers - 1
    while swapped:  # swappedがTrueである限りここに入ってきて　もしFalseだったら処理が終わる
        swapped = False
        # あとはバブルソートのやり方と同じ
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start = start + 1

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(nums)
    print(cocktail_sort(nums))
