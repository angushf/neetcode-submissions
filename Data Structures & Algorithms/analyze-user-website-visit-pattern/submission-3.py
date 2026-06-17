class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        map = {}
        map2 = {}
        count = 1

        visits = sorted(zip(username, timestamp, website))

        print(visits)

        for u, t, w in visits:
            map[u] = map.get(u, []) + [w]

        for username, pattern in map.items():
            if len(pattern) < 3:
                continue

            key = tuple(pattern[0:3])
            map2[key] = map2.get(key, 0) + 1

        best_pattern = None
        maxCount = 0

        for pattern, count in map2.items():
            if count > maxCount:
                best_pattern = pattern
                maxCount = count

            if count == maxCount and pattern < best_pattern:
                best_pattern = pattern

        print(map)

        return list(best_pattern) 