def selection_sort(array):
    for i in range(len(array) - 1):
        minimum = i
        for j in range(i, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[i], array[minimum] = array[minimum], array[i]


if __name__ == '__main__':
    import time

    def test1():
        import random
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 items...')
        t1 = time.time()
        selection_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l1 == l2

    test1()