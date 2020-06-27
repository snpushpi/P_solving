"""
STATEMENT
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
CLARIFICATIONS
- What happens when there is no solution? Assume solution exists.
- Can the list be empty? No.
- Is the list sorted? Not necessarily.
- Repeatation of elements?No
EXAMPLES
[2, 7, 11, 15], 9 -> [0,1]
"""
def two_sum(num_list, target):
    dict ={}
    l = len(num_list)
    for i in range(l):
        dict[num_list[i]]=i
        if target-num_list[i] in dict:
            return [i, dict[target - num_list[i]]]
print(two_sum([2, 7, 11, 15], 9))
        

