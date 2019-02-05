def kmp_search(s, pattern):
    slen = len(s)
    plen = len(pattern)
    lps = construct_lps(s)
    results = []

    i = 0
    j = 0
    while i < slen:
        if s[i] == pattern[j]:
            i += 1
            j += 1

            if j == plen:
                results.append(i - j)
                j = lps[j - 1]

        elif i < slen:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return results


def construct_lps(s):
    slen = len(s)
    lsp = [0] * slen

    i = 1
    prev_lsp_len = 0
    while i < slen:
        if s[i] == s[prev_lsp_len]:
            prev_lsp_len += 1
            lsp[i] = prev_lsp_len
        elif prev_lsp_len != 0:
            prev_lsp_len = lsp[prev_lsp_len - 1]
            continue
        else:
            lsp[i] = 0
        i += 1

    return lsp


if __name__ == '__main__':
    string = 'ABABDABACDABABCABAB'
    pattern = 'ABABCABAB'
    assert kmp_search(string, pattern) == [10]

    string = 'AAAAA'
    pattern = 'A'
    assert kmp_search(string, pattern) == [0, 1, 2, 3, 4]

    string = 'AAAAABAAABAAAA'
    pattern = 'AAAA'
    assert kmp_search(string, pattern) == [0, 1, 10]

    string = 'AABAACAADAABAABA'
    pattern = 'AABA'
    assert kmp_search(string, pattern) == [0, 9, 12]
