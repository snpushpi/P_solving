import heapq
def minimumMeetingrooms(Input):
    size = len(Input)
    if size<=1: return size
    heap = []
    result = 0
    for interval in sorted(intervals):
        while heap and heap[0]<=interval[0]:
            heapq.heappop(heap)
        heapq.heappush(heap,interval[1])
        result = max(result,interval[1])
    return result
print(minimumMeetingrooms([[0,30],[5,10],[15,20]]))
        

