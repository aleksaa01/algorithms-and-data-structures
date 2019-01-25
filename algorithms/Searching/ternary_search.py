def search_array(list_object, item):
    first = 0
    last = len(list_object) - 1

    while last >= first:
        mid1 = first + (last - first) // 3
        mid2 = last - (last - first) // 3
        mid1_item = list_object[mid1]
        mid2_item = list_object[mid2]

        if item == mid1_item or item == mid2_item:
            return True
        elif item < mid1_item:
            first = mid1 - 1
        elif item > mid1_item and item < mid2_item:
            first = mid1 + 1
            last = mid2 - 1
        else:
            first = mid2 + 1
    return False


if __name__ == '__main__':
    import time

    t1 = time.time()
    l = [i for i in range(1000000)]
    assert search_array(l, 999999) == True
    t2 = time.time()
    print('Ternary search: ', t2 - t1)