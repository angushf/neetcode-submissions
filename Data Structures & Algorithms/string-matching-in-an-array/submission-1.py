class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return []

        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                
                if words[i] in words[j]:
                    result.append(words[i])
                
        return list(set(result))