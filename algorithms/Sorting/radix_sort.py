def radix_sort(array, max_element=None):
    if max_element is None:
        max_element = max(array)

    mul = 1
    array_len = len(array)
    while max_element:
        count_sort(array, array_len, mul)
        mul *= 10
        max_element //= 10


def count_sort(array, array_len, pos):
    output = [0] * array_len
    count = [0] * 10

    for i in range(array_len):
        count[(array[i] // pos) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(array_len - 1, -1, -1):
        digit = (array[i] // pos) % 10
        output[count[digit] - 1] = array[i]
        count[digit] -= 1

    # why not just do: array = output | idk, can we ?
    for i in range(array_len):
        array[i] = output[i]


if __name__ == '__main__':
    import time
    import random

    def test1():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items, with 4999 being the max number, and passed max number...')
        t1 = time.time()
        radix_sort(l2, 4999)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l2 == l1

    def test2():
        l1 = [i for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items, with 4999 being the max number...')
        t1 = time.time()
        radix_sort(l2)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l2 == l1

    def test3():
        l1 = [random.randint(0, 49) for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items, with 49 being the max number, and passed max number...')
        t1 = time.time()
        radix_sort(l2, 49)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l2 == sorted(l1)

    def test4():
        l1 = [random.randint(0, 49) for i in range(5000)]
        l2 = l1.copy()
        random.shuffle(l2)
        print('Sorting 5000 unsorted items, with 49 being the max number...')
        t1 = time.time()
        radix_sort(l2, 49)
        t2 = time.time()
        print('Time took:', t2 - t1)
        assert l2 == sorted(l1)

    test1()
    test2()
    test3()
    test4()
