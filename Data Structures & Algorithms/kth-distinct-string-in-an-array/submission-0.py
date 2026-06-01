class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        countMap = Counter(arr)
        arr = []

        for key, count in countMap.items():
            if count == 1:
                arr.append(key)

        if len(arr) < k:
            return ""

        return arr[k-1]