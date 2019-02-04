def shiftbyk(s, k):
    slen = len(s)
    sres = [None] * slen

    for i in range(slen):
        sres[(i + k) % slen] = s[i]

    return ''.join(sres)


if __name__ == '__main__':
    a = 'test 123...'
    print(shiftbyk(a, 1))