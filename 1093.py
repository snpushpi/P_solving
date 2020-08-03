'''
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.
(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)
 
Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a substring of "cabac" because we can delete the first "c".
str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 
Note:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
'''
def lcs(str1, str2):
    dp = [[0 for i in range(len(str2))] for j in range(len(str1))]
    dp[0][0]= '' if str1[0]==str2[0] else str1[0]
    for i in range(1,len(str1)):
        dp[i][0]=dp[i-1][0] if str1[i]!=str2[0] else str2[0]
    for i in range(1,len(str2)):
        dp[0][i]=dp[0][i-1] if str2[i]!=str1[0] else str1[0]
    for i in range(1,len(str1)):
        for j in range(1,len(str2)):
            if str1[i]==str2[j]:
                if len(dp[i-1][j-1]+str1[i])>=max(len(dp[i-1][j]), len(dp[i][j-1])):
                    dp[i][j]=dp[i-1][j-1]+str1[i]
                elif len(dp[i-1][j])>=max(len(dp[i-1][j-1])+1, len(dp[i][j-1])):
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i][j-1]
            else:
                if len(dp[i-1][j])>=len(dp[i][j-1]):
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i][j-1]
    return dp[len(str1)-1][len(str2)-1]
def main(str1, str2):
    cs = lcs(str1, str2)
    print(cs)
    result = ""
    index1, index2 = 0,0
    for char in cs:
        while str1[index1]!=char:
            result+=str1[index1]
            index1+=1
        while str2[index2]!=char:
            result+=str2[index2]
            index2+=1 
        result+=char
        index1, index2=index1+1, index2+1
    return result+str1[index1:]+str2[index2:]
print(main('abac','cab'))





