'''
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''
def missing(num_list):
    result_list=[]
    l = len(num_list)
    for i in range(l-1):
        if not num_list[i+1]==num_list[i]+1:
            if num_list[i+1]==num_list[i]+2:
                result_list.append(num_list[i]+1)
            else:
                result_list.append([num_list[i]+1, num_list[i+1]-1])
    return result_list
