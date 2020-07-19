'''
	Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
	Note:
	The same word in the dictionary may be reused multiple times in the segmentation.
	You may assume the dictionary does not contain duplicate words.
	Example 1:
	Input: s = "leetcode", wordDict = ["leet", "code"]
	Output: true
	Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
def wordbreak(s, word_list):
    dp = [False for i in range(len(s)+1)]
    dp[0]= True
    for i in range(1,len(s)+1):
        for j in range(i, -1, -1):
            if dp[j] and s[j+1:i+1] in word_list:
                dp[i]=True
                break
    print(dp)
    return dp[len(s)]
print(wordbreak('leetcode', ['leet', 'code']))
