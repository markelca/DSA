

def bucketSort(nums):
    counts = [0, 0, 0]

    for num in nums:
        counts[num] += 1

    for i in range(len(nums)):
        for j in range(len(counts)):
            if counts[j] > 0:
                print('i', i)
                nums[i] = j
                counts[j] -= 1
                break



l = [2,1,1,2,0,1,0,2,1]

bucketSort(l)

print(l)


