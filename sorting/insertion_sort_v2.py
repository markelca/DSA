from typing import List


def sort(l: List[int]):
    for i in range(1, len(l)):
        j = i - 1
        while j >= 0 and l[j + 1] < l[j]:
            tmp = l[j + 1]
            l[j + 1] = l[j]
            l[j] = tmp
            j -= 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

l = [2,3,4,9,-1,6]
sort(l)
print(l)
