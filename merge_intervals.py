"""
STATEMENT
Given a collection of intervals, merge all overlapping intervals.
CLARIFICATIONS
- If two intervals touch on the boundary, are they considered overlapping? Yes.
- Are the intervals sorted in any way? Not necessarily.
- Are the intervals given as object instantiations of some class or an array of start and end?
  An object, define that too.
EXAMPLES
[1,3],[2,6],[8,10],[15,18] -> [1,6],[8,10],[15,18].
COMMENTS
- We should start with the leftmost interval possible. Let's sort the intervals by their start.
- Then we would iterate the list of intervals and merge until we get an interval whose start is
  at right of the current interval end.
- O(n log n) time complexity and O(n) space complexity, assuming in-place sort.
"""
def merge_sort(list):
    n = len(list)
    if n==1:
        return list
    half_n = int(n/2)
    left_list = list[:half_n]
    right_list = list[half_n:]
    ml = merge_sort(left_list)
    mr = merge_sort(right_list)
    left, right = 0,0
    result =[]
    while left<len(ml) and right<len(mr):
        if ml[left]<mr[right]:
            result.append(ml[left])
            left+=1
        else:
            result.append(mr[right])
            right+=1
    while left<len(ml):
        result.append(ml[left])
        left+=1
    while right<len(mr):
        result.append(mr[right])
        right+=1
    return result

def merge_interval(listi):
    list_we_merge = []
    check_dict = {}
    for elt in listi:
        list_we_merge+=elt
        if elt[0] not in check_dict:
            check_dict[elt[0]]=['s']
        else:
            check_dict[elt[0]].append('s')
        if elt[1] not in check_dict:
            check_dict[elt[1]]=['e']
        else:
            check_dict[elt[1]].append('e')
    sorted_list = merge_sort(list(set(list_we_merge)))
    s = 0
    e = 0
    result_list = []
    start = 0
    l = len(sorted_list)
    for i in range(l):
        s+=check_dict[sorted_list[i]].count('s')
        e+=check_dict[sorted_list[i]].count('e')
        if s==e:
            result_list.append([sorted_list[start],sorted_list[i]])
            start = i+1
    return result_list

print(merge_interval([[1,6],[6,8],[6,9]]))


