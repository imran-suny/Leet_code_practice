1. maxheap of counter > q for maxheap kkn available ([cnt, time + n]) # availale when  q[0][1] == time: hole maxheap a cnt add
Solution:    # see the explanation video from 9:41
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]   # time hobe q er second ta 
            else:
                cnt = 1 + heapq.heappop(maxHeap)   # -3, 2 , process korar pore count komabo... [-2, 2]
                if cnt:
                    q.append([cnt, time + n])      # [cnt, position + n]
            if q and q[0][1] == time:    # time =2, q = [-2,2], so -2 now availabe to process, so add it to the q
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


# Greedy algorithm
class Solution(object):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_count = max(counter.values())
        min_time = (max_count - 1) * (n + 1) + \
                    sum(map(lambda count: count == max_count, counter.values()))
    
        return max(min_time, len(tasks))
