def shellsort(array):
    gap = len(array) // 2
    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(array, start, gap)
        gap //= 2


def shellsort_improved(array):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for start in range(gap):
            gap_insertion_sort(array, start, gap)


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

    def test3():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items...(shellsort improved)')
        t1 = time.time()
        shellsort_improved(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test4():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('Sorting 5000 sorted items...(shellsort improved)')
        t1 = time.time()
        shellsort_improved(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    test1()
    test2()
    test3()
    test4()
