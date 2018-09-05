"""Implementations of the Merge sort algorithm."""


def merge_sort(numbers):
    """Split the numbers into left and right halves, sort those, then merge.

    This is the time-efficient but not space-efficient solution.
    """
    if len(numbers) < 2:
        return numbers
    elif len(numbers) == 2:
        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers
    else:
        middle = len(numbers) // 2
        left = merge_sort(numbers[:middle])
        right = merge_sort(numbers[middle:])
        output = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            elif left[i] > right[j]:
                output.append(right[j])
                j += 1
            else:
                output.append(left[i])
                i += 1

        if i == len(left):
            output.extend(right[j:])
        if j == len(right):
            output.extend(left[i:])
        return output


def merge_sort2(numbers):
    """Split the numbers into left and right halves, sort those, then merge.

    This is the space-efficient but not time-efficient solution.
    """
    if len(numbers) < 2:
        return numbers
    elif len(numbers) == 2:
        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers
    else:
        middle = len(numbers) // 2
        left = merge_sort(numbers[:middle])
        right = merge_sort(numbers[middle:])
        output = []

        while left and right:
            if left[0] < right[0]:
                output.append(left.pop(0))
            elif left[0] > right[0]:
                output.append(right.pop(0))
            else:
                output.append(left.pop(0))

        if left:
            while left:
                output.append(left.pop(0))
        if right:
            while right:
                output.append(right.pop(0))
        return output

if __name__ == "__main__":
    from timeit import timeit
    import random

    best_case = list(range(100))
    worst_case = list(range(100, 0, -1))
    avg_case = [random.randint(0, 100) for _ in range(100)]

    best_stmt = "from __main__ import merge_sort, best_case;merge_sort(best_case[:])"
    worst_stmt = "from __main__ import merge_sort, worst_case; merge_sort(worst_case[:])"
    avg_stmt = "from __main__ import merge_sort, avg_case; merge_sort(avg_case[:])"

    best_time = timeit(best_stmt, number=1000)
    worst_time = timeit(worst_stmt, number=1000)
    avg_time = timeit(avg_stmt, number=1000)

    print("For 1000 iterations of the time-efficient merge sort...")
    print(f"\t...the best case finished in {best_time} seconds")
    print(f"\t...the worst case finished in {worst_time} seconds")
    print(f"\t...the average (random) case finished in {avg_time} seconds")

    best_stmt = "from __main__ import merge_sort2, best_case;merge_sort2(best_case[:])"
    worst_stmt = "from __main__ import merge_sort2, worst_case; merge_sort2(worst_case[:])"
    avg_stmt = "from __main__ import merge_sort2, avg_case; merge_sort2(avg_case[:])"

    best_time = timeit(best_stmt, number=1000)
    worst_time = timeit(worst_stmt, number=1000)
    avg_time = timeit(avg_stmt, number=1000)

    print("For 1000 iterations of the space-efficient merge sort...")
    print(f"\t...the best case finished in {best_time} seconds")
    print(f"\t...the worst case finished in {worst_time} seconds")
    print(f"\t...the average (random) case finished in {avg_time} seconds")
