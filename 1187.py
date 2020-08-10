'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
 
Example 1:
Input: text = "nlaebolko"
Output: 1
Example 2:
Input: text = "loonbalxballpoon"
Output: 2
Example 3:
Input: text = "leetcode"
Output: 0
 
Constraints:
1 <= text.length <= 10^4
text consists of lower case English letters only.
'''
def main(text):
    b = text.count('b')
    l = text.count('l')
    a = text.count('a')
    o = text.count('o')
    n = text.count('n')
    min1 = min(b,a,n)
    min2 = min(l,o)
    if 2*min1<min2:
        return min1
    else:
        return min2//2
print(main("leetcode"))