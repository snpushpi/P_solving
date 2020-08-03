'''
Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.
 
Example 1:
Input: "cdadabcc"
Output: "adbc"
Example 2:
Input: "abcd"
Output: "abcd"
Example 3:
Input: "ecbacba"
Output: "eacb"
Example 4:
Input: "leetcode"
Output: "letcod"
 
Note:
1 <= text.length <= 1000
text consists of lowercase English letters.
'''
def smaller_subseq(text):
    n = len(text)
    dp = ['']*n
    dp[0]+=text[0]
    for i in range(1,n):
        if text[i] in dp[i-1]:
            ind = dp[i-1].index(text[i])
            print(dp[i-1][:ind]+dp[i-1][ind+1:]+text[i])
            if dp[i-1][:ind]+dp[i-1][ind+1:]+text[i]<dp[i-1]:
                dp[i]=dp[i-1][:ind]+dp[i-1][ind+1:]+text[i]
            else:
                dp[i]=dp[i-1]
        else:
            dp[i]=dp[i-1]+text[i]
    print(dp)
    return dp[n-1]
print(smaller_subseq("leetcode"))
