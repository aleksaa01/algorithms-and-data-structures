def bubble_sort(array):
    for x in range(len(array) - 1):
        for j in range(len(array) - x - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def bubble_sort_improved(array):
    x = 0
    n = len(array)
    while x < n - 1:
        swaped = False
        for j in range(n - x - 1):
            if array[j] > array[j + 1]:
                swaped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swaped:
            break
        x += 1


if __name__ == '__main__':
    import time
    import random

    def test1():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('(bubble sort) Sorting 5000 unsorted items...')
        t1 = time.time()
        bubble_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test2():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('(Improved bubble sort) Sorting 5000 unsorted items...')
        t1 = time.time()
        bubble_sort_improved(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test3():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('(bubble sort) Sorting 5000 sorted items...')
        t1 = time.time()
        bubble_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    def test4():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        print('(Improved bubble sort) Sorting 5000 sorted items...')
        t1 = time.time()
        bubble_sort_improved(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    test1()
    test2()
    test3()
    test4()