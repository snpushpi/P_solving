'''
Find the longest common subsequnce between two sequences 
'''
def lcs(str1, str2):
    dp = [[0 for i in range(len(str2))] for j in range(len(str1))]
    dp[0][0]=0 if str1[0]==str2[0] else 0
    for i in range(1,len(str1)):
        dp[i][0]=dp[i-1][0] if str1[i]!=str2[0] else 1
    for i in range(1,len(str2)):
        dp[0][i]=dp[0][i-1] if str2[i]!=str1[0] else 1
    for i in range(1,len(str1)):
        for j in range(1,len(str2)):
            if str1[i]==str2[j]:
                dp[i][j]=max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
    return dp[len(str1)-1][len(str2)-1]
print(lcs("abac","cab"))