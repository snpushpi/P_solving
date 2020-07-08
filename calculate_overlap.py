'''
	Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
	You may assume that the intervals were initially sorted according to their start times.
	Example 1:
	Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
	Output: [[1,5],[6,9]]
	Example 2:
	Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
	Output: [[1,2],[3,10],[12,16]]
	Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
def find_overlap(intervals,new_interval):
    l = len(intervals)
    start, end =0,0
    for i in range(l):
        if new_interval[0]<=intervals[i][0]:
            start= i
            break
    for i in range(l):
        if new_interval[1]<=intervals[i][0]:
            end = i
            break
    result_list = []
    if start==end:
        if intervals[start-1][1]>=new_interval[0]:
            if intervals[start-1][1]<new_interval[1]:
                intervals[start-1][1]=new_interval[1]
                result_list= intervals
            else:
                result_list = intervals
        else:
            result_list = intervals[:start]+[new_interval]+intervals[start:]
    else:
        if intervals[start-1][1]<new_interval[0]:
            if intervals[end-1][1]<new_interval[1]:
                result_list =  intervals[:start]+[new_interval]+intervals[end:]
            else:
                result_list = intervals[:start]+[[new_interval[0], intervals[end-1][0]]]+intervals[end:]
        else:
            if intervals[end-1][1]<new_interval[1]:
                result_list = intervals[:start-1]+[[intervals[start-1][0],new_interval[1]]]+intervals[end:]
            else:
                result_list = intervals[:start-1]+[[intervals[start-1][0],intervals[end-1][1]]]+intervals[end:]
    l = len(result_list)
    dummy = 0
    for i in range(l-1):
        if result_list[i][1]==result_list[i+1][0]:
            if i<=l-3 and result_list[i+1][1]==result_list[i+2][0]:
                lap = [result_list[i][0],result_list[i+2][1]]
                result_list[i]=lap
                return result_list[:i+1]+result_list[i+3:]
            else:
                lap = [result_list[i][0],result_list[i+1][1]]
                result_list[i]=lap
                return result_list[:i+1]+result_list[i+2:]
    return result_list           


print(find_overlap([[1,3],[6,9]],[2,5])) 