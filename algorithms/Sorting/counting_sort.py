def counting_sort(array, max_element=None):
    if max_element is None:
        k = max(array)
    else:
        k = max_element

    sorted_array = [0] * len(array)

    aux = [0] * (k + 1)
    for i in array:
        aux[i] += 1

    j = 0
    for i in range(k + 1):
        num = aux[i]
        while num > 0:
            sorted_array[j] = i
            j += 1
            num -= 1

    return sorted_array


if __name__ == '__main__':
    import time
    import random

    # Sorting already sorted array is going to be as fast as one that's not sorted.
    # Due to the nature of counting sort's algorithm.

    def test1():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items, with 4999 being the max number, and passed max number...')
        t1 = time.time()
        l2 = counting_sort(l2, 4999)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l2 == l1

    def test2():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items, with 4999 being the max number...')
        t1 = time.time()
        l2 = counting_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l2 == l1

    def test3():
        l1 = [random.randint(0, 49) for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items, with 49 being the max number, and passed max number...')
        t1 = time.time()
        l2 = counting_sort(l2, 49)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l2 == sorted(l1)

    def test4():
        l1 = [random.randint(0, 49) for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items, with 49 being the max number...')
        t1 = time.time()
        l2 = counting_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l2 == sorted(l1)

    test1()
    test2()
    test3()
    test4()
