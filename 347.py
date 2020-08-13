'''
	Given a non-empty array of integers, return the k most frequent elements.
	For example,
	Given [1,1,1,2,2,3] and k = 2, return [1,2]
'''
def main(nums,k):
    frequent = {}
    for elt in nums:
        if elt in frequent:
            frequent[elt]+=1
        else:
            frequent[elt]=1
    import heapq
    result = []
    heap = []
    for key, value in frequent.items():
        heapq.heappush(heap,(-value,key))
    for i in range(k):
        result.append(heapq.heappop(heap)[1])
    return result

print(main([1,1,1,2,2,3],2))