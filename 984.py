'''
Given two integers A and B, return any string S such that:
S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
 
Example 1:
Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
'''
def main(a,b):
    result_string = ''
    if a == b:
        for i in range(2*a):
            if i%2==0:
                result_string+='a'
            else:
                result_string+='b'
    big = b if b>a else a
    small = a if a<b else b
    if big==2*small+2:
        if big==b:
            for i in range(a):
                result_string+='bba'
            result_string+='bb'
        else:
            for i in range(a):
                result_string+='aab'
            result_string+='aa'
    elif big==2*small+1:
        if big==b:
            for i in range(a):
                result_string+='bba'
            result_string+='b'
        else:
            for i in range(a):
                result_string+='aab'
            result_string+='a'
    elif big==2*small:
        if big==b:
            for i in range(a):
                result_string+='bba'
        else:
            for i in range(a):
                result_string+='aab'
    elif big==2*small-1:
        if big==b:
            for i in range(a-1):
                result_string+='bba'
            result_string+='ba'
        else:
            for i in range(a-1):
                result_string+='aab'
            result_string+='ab'
    elif big==2*small-2:
        if big==b:
            for i in range(a-1):
                result_string+='bba'
            result_string+='a'
        else:
            for i in range(a-1):
                result_string+='aab'
            result_string+='b'
    else:
        n = small-2
        m = 1
        p = big-small+1
        q = 2*small-2-big
        list1 = []
        list2 = []
        if big==b:
            for i in range(p):
                list1.append('bb')
            for j in range(q):
                list1.append('b')
            for i in range(m):
                list2.append('aa')
            for j in range(n):
                list2.append('a')
            for i in range(m+n):
                result_string+=list1[i]+list2[i]
        else:
            for i in range(p):
                list1.append('aa')
            for j in range(q):
                list1.append('a')
            for i in range(m):
                list2.append('bb')
            for j in range(n):
                list2.append('b')
            for i in range(m+n):
                result_string+=list1[i]+list2[i]
    return result_string

print(main(5,9))

