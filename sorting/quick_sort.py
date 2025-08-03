


def quick_sort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s

    for i in range(s,e):
        if arr[i] <= pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    arr[e] = arr[left]
    arr[left] = pivot
    
    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1, e)
    
    return arr


arr = [6, 2, 4, 1, 3]

sorted_arr = quick_sort(arr, 0, 4)
print(sorted_arr)
