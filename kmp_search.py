def get_next_array(str):
    length = len(str)
    # 初始化长度为length的next数组
    next_array = [i for i in range(length)]
    next_array[0] = -1
    k = -1
    j = 0
    while j < length - 1:
        if k == -1 or str[j] == str[k]:
            j += 1
            k += 1
            if str[j] != str[k]:
                next_array[j] = k
            else:
                next_array[j] = next_array[k]
        else:
            k = next_array[k]
    return next_array


def kmp_search(target, sub):
    i = 0
    j = 0
    next_array = get_next_array(sub)
    while i < len(target) and j < len(sub):
        if j == -1 or target[i] == sub[j]:
            i += 1
            j += 1
        else:
            j = next_array[j]
    if j == len(sub):
        return i - j
    else:
        return -1


src = "BBC ABCDAB ABCDABCDABDE"
target = "ABCDABD"
print(kmp_search(src, target))
