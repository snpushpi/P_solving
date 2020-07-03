'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:
All given inputs are in lowercase letters a-z.
'''
def lcp(strs):
    def isprefix(strs,index):
        prefix = strs[0][:index]
        for str in strs:
            if not str.startswith(prefix):
                return False
        return True
    if not strs:
        return ""
    minlength = float('inf')
    for string in strs:
        minlength = min(minlength,len(string))
    print(minlength)
    low, high = 0, minlength
    while low<=high:
        mid = int((low+high)/2)
        if isprefix(strs,mid):
            low = mid+1
        else:
            high = mid-1
    return strs[0][:int((low+high)/2)]
print(lcp(["flower","flow","flight"]))
