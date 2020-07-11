'''
	Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
	Example 1:
	Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
	Output: true
	Example 2:
	Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
	Output: false
'''
def isinterleave(s1, s2, s3):
    marker1 = 0
    marker2 = 0
    check_dict = {s1:marker1, s2:marker2}
    if s3[0]==s1[0]:
        runner = s1
        stopper = s2
    else:
        runner = s2
        stopper = s1
    for i in range(len(s3)):
        print(i)
        if check_dict[runner]<=len(runner)-1 and s3[i]==runner[check_dict[runner]]:
            check_dict[runner]+=1
        elif check_dict[stopper]<=len(stopper)-1 and s3[i]==stopper[check_dict[stopper]]:
            runner, stopper = stopper, runner 
            check_dict[runner]+=1
        else:
            print(i)
            return False
    return True
print(isinterleave("aabcc","dbbca","aadbbbaccc"))
        