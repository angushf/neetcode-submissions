class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                # we have reused all words and ended up with an empty string
                return True

            if not any(s[i:].startswith(w[0]) for w in wordSet):
                # no word in dict starts with the same letter as s[i]
                return False

            if cache[i] != -1:
                return cache[i]

            ways = False
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        ways = True

            cache[i] = ways

            return cache[i]

        print(cache)
        return dfs(0)