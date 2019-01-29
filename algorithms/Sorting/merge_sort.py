def merge_sort(array):
    if len(array) < 2:
        return

    mid = len(array) // 2
    lpart = array[:mid]
    rpart = array[mid:]

    merge_sort(lpart)
    merge_sort(rpart)

    i = 0
    j = 0
    k = 0

    while i < len(lpart) and j < len(rpart):
        if lpart[i] < rpart[j]:
            array[k] = lpart[i]
            i += 1
        else:
            array[k] = rpart[j]
            j += 1
        k += 1

    while i < len(lpart):
        array[k] = lpart[i]
        i += 1
        k += 1

    while j < len(rpart):
        array[k] = rpart[j]
        j += 1
        k += 1


def merge_sort_improved(array, start, end):
    # technically this should be faster, because there is not array slicing.
    if end - start < 2:
        return

    mid = (start + end) // 2
    merge_sort_improved(array, start, mid)
    merge_sort_improved(array, mid, end)

    temp_array = [None] * (end - start)
    i = start
    j = mid
    k = 0

    for _ in range(end - start):
        if j >= end:
            temp_array[k] = array[i]
            i += 1
        elif i >= mid:
            temp_array[k] = array[j]
            j += 1
        elif array[i] < array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            j += 1
        k += 1

    for x in range(k):
        array[start] = temp_array[x]
        start += 1


if __name__ == '__main__':
    import time
    import random

    def test1():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items...')
        t1 = time.time()
        merge_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test2():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('Sorting 5000 sorted items...')
        t1 = time.time()
        merge_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test3():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items...(merge sort improved)')
        t1 = time.time()
        merge_sort_improved(l2, 0, len(l2))
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test4():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('Sorting 5000 sorted items...(merge sort improved)')
        t1 = time.time()
        merge_sort_improved(l2, 0, len(l2))
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    test1()
    test2()
    test3()
    test4()
