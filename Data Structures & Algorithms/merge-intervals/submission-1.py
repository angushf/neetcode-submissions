class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        out = []

        for s,e in intervals:
            if out and out[-1][1] >= s:
                out[-1][1] = max(out[-1][1], e)
            else:
                out.append([s,e]) 


        return out