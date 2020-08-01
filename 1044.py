'''
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)
Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)
 
Example 1:
Input: "banana"
Output: "ana"
Example 2:
Input: "abcd"
Output: ""
 
Note:
2 <= S.length <= 10^5
S consists of lowercase English letters.
'''
def substring(s):
    l = len(s)
    for i in range(l-2,0,-1):
        temp_set = set()
        for j in range(l-i):
            if s[j:j+i+1] in temp_set:
                return s[j:j+i+1]
            else:
                temp_set.add(s[j:j+i+1])
    return ""
print(substring("abababa"))
            
