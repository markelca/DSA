def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    m = (e + s) // 2

    mergeSort(arr, s, m)

    mergeSort(arr, m + 1, e)

    merge(arr, s, m, e)

    return arr

def merge(arr, s, m, e):
    l = arr[s:m+1]
    r = arr[m+1:e+1]

    i = 0
    j = 0
    k = s

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

    return arr


arr = [3,2,4,1,6]

mergeSort(arr, 0, len(arr))

print(arr)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
