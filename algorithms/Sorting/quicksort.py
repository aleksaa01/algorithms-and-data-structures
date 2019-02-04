def quicksort_improved(array, start, end):
    quicksort_helper(array, start, end - 1)


def quicksort_helper(array, start, end):
    if end - start < 1:
        return

    pivot = partition_improved(array, start, end)
    quicksort_helper(array, start, pivot)
    quicksort_helper(array, pivot + 1, end)


def partition_improved(array, start, end):
    pivot = array[(start + end) // 2]
    left = start
    right = end

    while True:
        # goes on until the condition in while loop is False,
        # or until value is same as pivot, which guarantees that loop will stop before going out of bounds.
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left >= right:
            return right

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


def quicksort(array, start, end):
    if end - start < 2:
        return

    pivot = partition(array, start, end - 1)
    quicksort(array, start, pivot)
    quicksort(array, pivot + 1, end)


def partition(array, start, end):
    # swap last and middle element, improvement for already sorted arrays.
    middle = (start + end + 1) // 2
    array[end], array[middle] = array[middle], array[end]

    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i


if __name__ == '__main__':
    import time
    import random

    def test1():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items...(quicksort)')
        t1 = time.perf_counter()
        quicksort(l2, 0, len(l2))
        t2 = time.perf_counter()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test2():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('Sorting 5000 sorted items...(quicksort)')
        t1 = time.perf_counter()
        quicksort(l2, 0, len(l2))
        t2 = time.perf_counter()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test3():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items...(quicksort improved)')
        t1 = time.perf_counter()
        quicksort_improved(l2, 0, len(l2))
        t2 = time.perf_counter()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test4():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('Sorting 5000 sorted items...(quicksort improved)')
        t1 = time.perf_counter()
        quicksort_improved(l2, 0, len(l2))
        t2 = time.perf_counter()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test5():
        l1 = [5, 4, 3, 3, 2, 1]
        l2 = l1.copy()
        quicksort_improved(l2, 0, len(l2))
        assert sorted(l1) == l2

    def test6():
        l1 = [5, 4, 3, 3, 2, 1]
        l2 = l1.copy()
        quicksort(l2, 0, len(l2))
        assert sorted(l1) == l2

    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
