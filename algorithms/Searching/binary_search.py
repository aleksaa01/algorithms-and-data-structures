def search_array(list_object, item):
    first = 0
    last = len(list_object) - 1

    while last >= first:
        midpoint = (first + last) // 2
        midpoint_item = list_object[midpoint]
        if midpoint_item == item:
            return True
        elif midpoint_item < item:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return False


def search_array_recursive1(array, item):
    # slower then version 2, because of list slicing.
    array_length = len(array)
    if array_length == 0:
        return False

    midpoint = array_length // 2

    midpoint_item = array[midpoint]
    if midpoint_item == item:
        return True
    elif midpoint_item < item:
        return search_array_recursive1(array[midpoint + 1:], item)
    else:
        return search_array_recursive1(array[:midpoint], item)


def search_array_recursive2(array, item, first, last):
    if first >= last:
        return False

    midpoint = (first + last) // 2

    midpoint_item = array[midpoint]
    if midpoint_item == item:
        return True
    elif midpoint_item < item:
        return search_array_recursive2(array, item, midpoint + 1, last)
    else:
        return search_array_recursive2(array, item, first, midpoint - 1)


if __name__ == '__main__':
    import time

    t1 = time.time()
    l = [i for i in range(1000000)]
    assert search_array(l, 999999) == True
    t2 = time.time()
    print('Binary search: ', t2 - t1)

    t1 = time.time()
    l = [i for i in range(1000000)]
    assert l.index(999999) > -1
    t2 = time.time()
    print('Python\'s index method: ', t2 - t1)

    t1 = time.time()
    l = [i for i in range(1000000)]
    assert search_array_recursive1(l, 999999) == True
    t2 = time.time()
    print('Recursive binary search (1): ', t2 - t1)

    t1 = time.time()
    l = [i for i in range(1000000)]
    assert search_array_recursive2(l, 999999, 0, len(l)) == True
    t2 = time.time()
    print('Recursive binary search (2): ', t2 - t1)
