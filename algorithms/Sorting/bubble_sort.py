def bubble_sort(array):
    for x in range(len(array) - 1):
        for j in range(len(array) - x - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == '__main__':
    import time

    def test1():
        import random
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 items...')
        t1 = time.time()
        bubble_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    test1()