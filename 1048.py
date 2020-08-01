'''
Given a list of words, each word consists of English lowercase letters.
Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
Return the longest possible length of a word chain with words chosen from the given list of words.
 
Example 1:
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 
Note:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
'''
import collections
def longeststrchain(input_list):
    dp = collections.defaultdict(int)
    input_list.sort(key=len)
    result = 0
    for word in input_list:
        for index in range(len(word)):
            temp_word = word[:index]+word[index+1:]
            if temp_word in dp:
                dp[word]=max(dp[temp_word]+1,dp[word])
            else:
                dp[word]=max(dp[word],1)
        result = max(result,dp[word])
    return result
print(longeststrchain(["a","b","ba","bca","bda","bdca"]))        