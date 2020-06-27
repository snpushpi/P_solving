"""
STATEMENT
Given a string and a number of rows, pring the string in a zigzag fashion across rows.
"PAYPALISHIRING" can be written as the following in 3 rows:
P   A   H   N
A P L S I I G
Y   I   R
CLARIFICATIONS
- Can I assume row number to be positive? Yes.
- For row number 1, it prints the identical string, right? Yes.
EXAMPLES
The given example looks OK to begin with.
COMMENTS
- We can initiate the rows as list of empty strings.
- We divide the given string in number of rows, and then print them with alternating direction in the rows.
- O(n) time complexity and (technically) O(n) space complexity.
- Our solution may involve slicing strings, which are technically in order of size of the string, but let's not worry about that right now.
  Python optimizes string slicing pretty well.
"""
def zigzag(s):
    l = len(s)
    first_list = []
    first_list.append(s[0])
    second_list =[]
    third_list =[]
    for i in range(1,l):
        if i%4==1 or i%4==3:
            second_list.append(s[i])
        elif i%4==2:
            third_list.append(s[i])
        else:
            first_list.append(s[i])

    print("   ".join(map(str, first_list)))
    print(" ".join(map(str, second_list)))
    print("   ".join(map(str, third_list)))

print(zigzag("PAYPALISHIRING"))