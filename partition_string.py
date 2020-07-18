'''
	Given a string s, partition s such that every substring of the partition is a palindrome.
	Return all possible palindrome partitioning of s.
'''
def partition(s):
    result = []
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
    return result
print(partition('bobobib'))
