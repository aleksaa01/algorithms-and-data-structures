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

    test1()
    test2()
