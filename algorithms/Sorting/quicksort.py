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
        t1 = time.time()
        quicksort(l2, 0, len(l2))
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test2():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('Sorting 5000 sorted items...(quicksort)')
        t1 = time.time()
        quicksort(l2, 0, len(l2))
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    test1()
    test2()
