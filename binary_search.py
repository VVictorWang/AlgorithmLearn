def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (int)((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


myList = [1, 5, 7, 8, 78, 190]
print(binary_search(myList, 780))
