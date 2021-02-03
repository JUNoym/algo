# o(log(n))のコード　再帰的に収束　安定ソート
def func2(n):
    if n <= 1:  # 最終的にここに収束する
        return
    else:
        print(n)
        func2(n/2)


func2(10)

# O(n)


def func3(numbers):
    for num in numbers:
        print(num)


func3([1, 2, 3, 4, 5])


# O(n * log(n))

def func4(n):
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return
    func4(n/2)


func4(10)
