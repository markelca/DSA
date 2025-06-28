# url: https://neetcode.io/problems/insertionSort
# Definition for a pair.
from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"Pair(key={self.key}, value={self.value})"

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        res.append(pairs)
        for i in range(1,len(pairs)):
            j = i - 1
            # print(pairs[j])
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                tmp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = tmp
                j -= 1
        res.append(pairs)

        return res

pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]
obs = [Pair(p[0],p[1]) for p in pairs]

res = Solution().insertionSort(obs)
for p in  res:
    print(p)
