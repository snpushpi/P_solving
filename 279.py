'''
	Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
	Example 1:
	Input: n = 12
	Output: 3 
	Explanation: 12 = 4 + 4 + 4.
	Example 2:
	Input: n = 13
	Output: 2
	Explanation: 13 = 4 + 9.
'''
import math
def main(n):
    c = math.sqrt(n)
    sqr_list = []
    for i in range(c+1):
        sqr_list.append(i*i)
    mapping = {sqr:1 for sqr in sqr_list}
    for i in range(n):
        if i not in mapping:
            mapping[i]=float('inf')
            for elt in sqr_list:
                if i>=elt:
                    mapping[i]=min(mapping[i],1+mapping[i-elt])
    return mapping[n]


