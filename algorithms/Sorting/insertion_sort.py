def insertion_sort(array):
    for i in range(len(array)):
        temp = array[i]
        j = i
        while j > 0 and temp < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp


if __name__ == '__main__':
    import time
    import random

    def test1():
        import random
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items...')
        t1 = time.time()
        insertion_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test2():
        import random
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('Sorting 5000 sorted items...')
        t1 = time.time()
        insertion_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    test1()
    test2()
