"""Implementation of the Insertion sort algorithm."""


def insertion_sort(numbers):
    """Iterate through the numbers and if number i < i - 1, move it to where it belongs."""
    if len(numbers) < 2:
        return numbers
    for i in range(1, len(numbers)):
        while numbers[i] < numbers[i - 1]:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            if (i - 1) == 0:
                break
            i -= 1
    return numbers


if __name__ == "__main__":
    from timeit import timeit
    import random

    best_case = list(range(100))
    worst_case = list(range(100, 0, -1))
    avg_case = [random.randint(0, 100) for _ in range(100)]

    best_stmt = "from __main__ import insertion_sort, best_case;insertion_sort(best_case[:])"
    worst_stmt = "from __main__ import insertion_sort, worst_case; insertion_sort(worst_case[:])"
    avg_stmt = "from __main__ import insertion_sort, avg_case; insertion_sort(avg_case[:])"

    best_time = timeit(best_stmt, number=1000)
    worst_time = timeit(worst_stmt, number=1000)
    avg_time = timeit(avg_stmt, number=1000)

    print("For 1000 iterations...")
    print(f"\t...the best case finished in {best_time} seconds")
    print(f"\t...the worst case finished in {worst_time} seconds")
    print(f"\t...the average (random) case finished in {avg_time} seconds")
