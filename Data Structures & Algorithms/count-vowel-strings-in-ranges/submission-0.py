class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        mySet = set()

        result = []

        for li, ri in queries:
            count = 0
            for i in range(li, ri + 1):
                if i in mySet:
                    count += 1
                else:
                    word = words[i]
                    if word[0] in vowels and word[-1] in vowels:
                        count += 1
                        mySet.add(i)
            result.append(count)

        return result
                    