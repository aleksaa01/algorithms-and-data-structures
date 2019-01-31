def shellsort(array):
    gap = len(array) // 2
    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(array, start, gap)
        gap //= 2


def gap_insertion_sort(array, start, gap):
    for i in range(start + gap, len(array), gap):
        elem = array[i]
        j = i - gap
        while j >= start and elem < array[j]:
            array[j + gap] = array[j]
            j -= gap
        array[j + gap] = elem


if __name__ == '__main__':
    import time
    import random

    def test1():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items...(shellsort)')
        t1 = time.time()
        shellsort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test2():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('Sorting 5000 sorted items...(shellsort)')
        t1 = time.time()
        shellsort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    test1()
    test2()
