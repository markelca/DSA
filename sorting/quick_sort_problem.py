


from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"({self.key}, {self.value})"

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.solution(pairs, 0, len(pairs) - 1)

    def solution(self, pairs: List[Pair], s: int, e: int):
        if e - s + 1 <= 1:
            return pairs

        pivot = pairs[e]
        left = s

        for i in range(s, e):
            if pairs[i].key <= pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1

        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.solution(pairs, s, left - 1)
        self.solution(pairs, left + 1, e)

        return pairs


pairs = [Pair(3, "cat"), Pair(2, "dog"), Pair(3, "bird")]

sorted = Solution().quickSort(pairs)

for x in pairs:
    print(x)

