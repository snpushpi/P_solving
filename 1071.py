'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)
Return the largest string X such that X divides str1 and X divides str2.
 
Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
 
Note:
1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
'''
def gcdoftsrings(str1, str2):
    if len(str1)>len(str2):
        str1, str2 = str2, str2 
    l_str1 = len(str1)
    for index in range(len(str1),0,-1):
        if l_str1%index!=0:
            continue
        substring_size = int(l_str1/index)
        substring1 = str1
        substring2 = str2
        check_string = str1[:substring_size]
        while check_string == substring1[:substring_size]:
            substring1 = substring1[substring_size:]
        while check_string == substring2[:substring_size]:
            substring2 = substring2[substring_size:]
        if substring1=="" and substring2=="":
            return check_string
    return ""
print(gcdoftsrings('LEET','CODE'))
