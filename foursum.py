"""
STATEMENT
Given an array S integers and a target, find all unique quadruplets a, b, c, and d in S such that a + b + c + d = target.
CLARIFICATIONS
- Similar clarifications as 015-3sum.
EXAMPLES
[1, 0, -1, 0, -2, 2], 0 =>
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
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
    return list(result_set)


def threesum(target, num_list):
    '''returns the list of tuples which sum up to the target'''
    result_set = set()
    l = len(num_list)
    for i in range(l):
        temp_result_list = two_sum(target-num_list[i], num_list[:i]+num_list[i+1:])
        for elt in temp_result_list:
            result_set.add(elt+(num_list[i],))
    return list(result_set)

def unique_determiner(tup,dict):
    check_set = {tup[i] for i in range(len(tup))}
    for elt in dict:
        if {elt[i] for i in range(len(elt))}==check_set:
            return False
    return True
def foursum(target, num_list):
    result_set = set()
    l = len(num_list)
    for i in range(l):
        temp_result_list = threesum(target-num_list[i], num_list[:i]+num_list[i+1:])
        for elt in temp_result_list:
            result_set.add(elt+(num_list[i],))
    final_result_dict = {}
    for elt in result_set:
        if elt not in final_result_dict and unique_determiner(elt, final_result_dict):
            final_result_dict[elt]=elt
    return list(final_result_dict.values())
    
print(foursum(0,[1, 0, -1, 0, -2, 2]))