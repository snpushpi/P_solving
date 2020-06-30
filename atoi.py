"""
STATEMENT
Implement atoi to convert a string to an integer.
CLARIFICATIONS
- Is there some basic conditions, such as how to
  handle whitespaces or non-digit characters? Ignore all whitespaces at start,
  then get the number and ignore the rest.
- What should the output for a string that is not an integer? Return 0.
- Should we assume the integer is 32 bit? Yes, for outside range, return 0.
EXAMPLES
"213" -> 213
"-1.6" -> -2
"0" -> 0
"112aeqwe" -> 112
COMMENTS
- The number can be negative.
- It can be a float, if the first digit after the point is more than or equal 5,
  the output would be incremented.
"""
def myatoi(str):
    str = str.split(' ')
    print(str)
    l = len(str)
    start =0
    sign = 1
    return_val = 0
    if str[0:1] in ['+','-']:
        start = 1
        if str[0:1]=='+':
            sign=1
        else:
            sign=-1
    for i in range(start,l):
        s = str[i:i+1]
        print(s)
        if s in ['0','1','2','3','4','5','6','7','8','9']:
            return_val= 10*return_val+ord(s)-ord('0')
        elif s ==".":
            if str[i+1:i+2] in ['0','1','2','3','4','5','6','7','8','9'] and str[i+1:i+2]>'5':
                return_val+=1
        else:
            break
    return_val*=sign
    return return_val

print(myatoi('123ehjjj'))


