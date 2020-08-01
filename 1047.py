'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
 
Example 1:
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 
Note:
1 <= S.length <= 20000
S consists only of English lowercase letters.
'''
def removeDuplicate(s):
    stack=[s[0]]
    for i in range(1,len(s)):
        if len(stack)>=1 and s[i]==stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack==[]:
        return ""
    else:
        string = ""
        for elt in stack:
            string+=elt
        return string
print(removeDuplicate('abbaca'))