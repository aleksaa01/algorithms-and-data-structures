def substring_sort(s, begin, end):
    return sort(s, begin, end)

def sort(s, begin, end):
    stemp = list(s[begin:end+1])
    quicksort(stemp, 0, len(stemp) - 1)
    return s[:begin] + ''.join(stemp) + s[end+1:]


def quicksort(array, start, end):
    if end - start < 1:
        return

    pivot = partition_reverse(array, start, end)
    quicksort(array, start, pivot)
    quicksort(array, pivot + 1, end)


def partition_reverse(array, start, end):
    pivot = array[(start + end) // 2]
    i = start
    j = end
    while True:
        while array[i] > pivot:
            i += 1

        while array[j] < pivot:
            j -= 1

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1



if __name__ == '__main__':
    s = 'hlleo'
    s = substring_sort(s, 1, 3)
    assert s == 'hlleo'

    s = 'ooneefspd'
    s = substring_sort(s, 0, 8)
    assert s == 'spoonfeed'

    s = 'effort'
    s = substring_sort(s, 1, 4)
    assert s == 'erofft'
