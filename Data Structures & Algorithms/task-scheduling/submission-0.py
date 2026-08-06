class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [(-freq, task) for task, freq in count.items()]
        heapq.heapify(max_heap)

        cooldown_q = deque()
        t = 0
        result = 0
        while max_heap or cooldown_q:
            if cooldown_q:
                # popleft from q and add to max_heap
                if cooldown_q[0][0] <= t:
                    t_avail, freq, task = cooldown_q.popleft()
                    heapq.heappush(max_heap, (-freq, task))

            # pull from max_heap
            if max_heap:
                freq, task = heapq.heappop(max_heap)
                if -freq - 1 > 0:
                    cooldown_q.append((t + (n+1), (-freq) - 1, task))
            
            result += 1
            t += 1

        return result
