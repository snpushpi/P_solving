'''
	Given two binary strings, return their sum (also a binary string).
	The input strings are both non-empty and contains only characters 1 or 0.
	Example 1:
	Input: a = "11", b = "1"
	Output: "100"
	Example 2:
	Input: a = "1010", b = "1011"
	Output: "10101"
'''
def binary_sum(a,b):
    result = ""
    carry = 0
    len_a, len_b = len(a)-1, len(b)-1
    while len_a>=0 and len_b>=0:
        result = (int(a[len_a])+int(a[len_b])+carry)%2+result
        carry = int((int(a[len_a])+int(b[len_b])+carry)/2)
        len_a-=1
        len_b-=1
    while len_a>=0:
        result = (int(a[len_a])+carry)%2+result
        carry = int((int(a[len_a])+carry)/2)
        len_a-=1
    while len_b>=0:
        result = (int(b[len_b])+carry)%2+result
        carry = int((int(b[len_b])+carry)/2)
        len_b-=1
    return result


