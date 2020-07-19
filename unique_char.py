'''
Given a string, find the longest substring that contains only two unique characters. For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique character is "bcbbbbcccb".
'''
def unique_char(s):
    l = len(s)
    dp1 = [{} for e in range(l)]
    dp1[0][s[0]]=1
    for i in range(1,l):
        if s[i]==s[i-1]:
            dp1[i][s[i]]=dp1[i-1][s[i-1]]+1
        else:
            dp1[i][s[i]]=1
    print(dp1)
    dp2 = [{} for e in range(l)]
    dp2[0][(s[0],)]=1
    for i in range(1,l):
        if s[i]==s[i-1]:
            dp2[i]={tuple(dp2[i-1].keys())[0]:dp2[i-1][tuple(dp2[i-1].keys())[0]]+1}
        else:
            if s[i] in tuple(dp2[i-1].keys())[0]:
                dp2[i]={tuple(dp2[i-1].keys())[0]:dp2[i-1][tuple(dp2[i-1].keys())[0]]+1}
            else:
                dp2[i]={(s[i],s[i-1]):dp1[i-1][s[i-1]]+1}
    print(dp2)
print(unique_char("abcbbbbcccbdddadacb"))
