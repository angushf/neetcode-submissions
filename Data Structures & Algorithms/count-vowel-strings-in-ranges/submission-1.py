class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'o', 'u', 'e', 'i'])
        binArr = []

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                binArr.append(1)
            else:
                binArr.append(0)

        prefix = [0]

        for i in range(len(binArr)):
            val = prefix[-1] + binArr[i]
            prefix.append(val)

        result = []
        for query in queries:
            li, ri = query
            answer = prefix[ri+1] - prefix[li]
            result.append(answer)

        return result

