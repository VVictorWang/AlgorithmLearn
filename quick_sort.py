def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        selected_index = (int)((len(array) - 1) / 2)
        selected = array[selected_index]
        left = [i for i in array if i <= selected]
        left.remove(selected)
        right = [i for i in array if i > selected]
        return quick_sort(left) + [selected] + quick_sort(right)


print(quick_sort([10, 89, 362, 1, 324, 324, 898, 3, 54, 32425]))
array = [1, 345, 234, 235, 3456, 345, 234]
print(quick_sort(array))
print(array)
