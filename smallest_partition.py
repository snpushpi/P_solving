'''
	Given a string s, partition s such that every substring of the partition is a palindrome.
	Return the minimum cuts needed for a palindrome partitioning of s.
	Example:
	Input: "aab"
	Output: 1
	Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
def partition(s):
    result = []
    minimum= float('inf')
    def isPalindrome(s):
        l = len(s)/2
        for i in range(int(l)):
            if s[i]!=s[-(i+1)]:
                return False
        return True
    def stringcheck(s, curr, i):
        if i==len(s):
            result.append(curr)
        for j in range(i, len(s)):
            if isPalindrome(s[i:j+1]):
                stringcheck(s, curr + [s[i:j+1]],j+1)
    stringcheck(s,[],0)
    for elt in result:
        if len(elt)<minimum:
            minimum=len(elt)
    return minimum-1
print(partition('bobobib'))