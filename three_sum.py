"""
STATEMENT
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all the unique triplets.
CLARIFICATIONS
- Do I return tuple of elements of their indexes? Elements.
- The solution may not exist, right? Yes.
- By unique, you mean, each tuple should be considered as set and then unique set of sets? Yes.
EXAMPLES
[-1, 0, 1, 2, -1, -4] ->
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
import collections
def two_sum(sum, num_list):
    '''given a number list and a sum, we try to find whether 
    we have any two numbers in that num_list that sum up to that number.
    '''
    result_set = set()
    num_set = set(num_list)
    for elt in num_set:
        if sum-elt in num_set:
            if elt!=sum-elt:
                result_set.add((elt,sum-elt))
            else:
                if num_list.count(elt)>=2:
                    result_set.add((elt,sum-elt))
    return result_set


def threesum(num_list):
    sum3_result_set = set()
    compl_list = []
    for elt in num_list:
        compl_list.append(-elt)
    print(compl_list)
    l = len(compl_list)
    for i in range(l):
        check_list = num_list[:i]+num_list[i+1:]
        result_set = two_sum(compl_list[i],check_list)
        if len(result_set)!=0:
            for elt in result_set:
                sum3_result_set.add(elt+(num_list[i],))
    print(sum3_result_set)
    final_dict = {}
    for elt in sum3_result_set:
        if elt not in final_dict and (elt[1],elt[0]) not in final_dict:
            final_dict[tuple(set(elt))]=elt
    return list(final_dict.values())
print(threesum([-1, 0, 1, 2, -1, -4]))
