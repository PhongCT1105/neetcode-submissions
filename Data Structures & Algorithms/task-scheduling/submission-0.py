class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        count_task = Counter(tasks)
        heap = [-cnt for cnt in count_task.values()]
        
        import heapq
        heapq.heapify(heap)
        idle = []
        time = 0

        while heap or idle:
            time += 1

            if heap:
                curr_max = heapq.heappop(heap) + 1
                if curr_max < 0:
                    idle.append((curr_max, time+n))
            
            if idle:
                if idle[0][1] == time: #Done wait
                    done_wait = idle.pop(0)
                    heapq.heappush(heap, done_wait[0])
        
        return time