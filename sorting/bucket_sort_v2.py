def bucketSort(arr):
    counts = [0, 0, 0]

    for num in arr:
        counts[num] += 1

    result = []
    for i in range(0, len(counts)):
        result += [i] * counts[i]

    return result

l = [2,1,1,2,0,1,0,2,1]

print(bucketSort(l))
