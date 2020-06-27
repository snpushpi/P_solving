"""
STATEMENT
Given a string s, find the longest palindromic substring in s.
CLARIFICATIONS
- If there is no palindrome that is more than one character, we can report
  any character? Yes.
EXAMPLES
"babad" -> "bab"
"cbbd" -> "bb"
COMMENTS
- We can keep a cache to store the result for all possible substring.
- Technically, the cache can be a list of list, but since the cache is half filled,
  we can keep a dictionary of dictionaries.
- O(n^2) time complexity and O(n^2) space complexity.
"""
def longest_palindrome(s):
    mem = {}
    l = len(s)
    for i in range(l-1):
        mem[(i,i+1)]= (s[i]==s[i+1])
    for i in range(l-2):
        mem[(i,i+2)]= (s[i]==s[i+2])
    for j in range(3,l):
        for i in range(l-j):
            mem[(i,i+j)]= (s[i]==s[i+j-1]) & (mem[(i+1,i+j-1)])
    return max(mem, key=mem.get)
print(longest_palindrome("cbabad"))
   