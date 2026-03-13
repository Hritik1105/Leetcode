import heapq

class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        
        heap = []
        
        for i, t in enumerate(workerTimes):
            heapq.heappush(heap, (t, i, 1))
        
        time = 0
        
        while mountainHeight > 0:
            currTime, worker, k = heapq.heappop(heap)
            
            time = currTime
            mountainHeight -= 1
            
            nextTime = currTime + workerTimes[worker] * (k + 1)
            
            heapq.heappush(heap, (nextTime, worker, k + 1))
        
        return time