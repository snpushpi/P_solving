'''
	A message containing letters from A-Z is being encoded to numbers using the following mapping:
	'A' -> 1
	'B' -> 2
	...
	'Z' -> 26
	Given a non-empty string containing only digits, determine the total number of ways to decode it.
	Example 1:
	Input: "12"
	Output: 2
	Explanation: It could be decoded as "AB" (1 2) or "L" (12).
	Example 2:
	Input: "226"
	Output: 3
	Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''
def map(s):
    if s[0]=='0' or len(s)==0:
        return 0
    if len(s)==1:
        return 1
    for i in range(1,len(s)):
        if s[i]=='0' and int(s[i-1])>=3:
            return 0
    dp = [0]*len(s)
    if int(s[:2])>26:
        dp[1]=1
    else:
        if s[1]=='0':
            dp[1]=1
        else:
            dp[1]=2
            dp[0]=1
    for index in range(2, len(s)):
        if s[index-1]=='0' or int(s[index-1]+s[index])>26:
            dp[index]=dp[index-1]
        elif s[index]=='0':
            dp[index]=dp[index-2]
        else:
            dp[index]=dp[index-1]+dp[index-2]
    return dp[len(s)-1]
print(map('2268'))
