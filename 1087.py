'''
A string S represents a list of words.
Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].
Return all words that can be formed in this manner, in lexicographical order.
 
Example 1:
Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:
Input: "abcd"
Output: ["abcd"]
 
Note:
1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
'''
def generate_list(my_string):
    brace = 0
    stack = []
    temp_stack=[]
    temp_string = ''
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    for char in my_string:
        if char=='{':
            brace=1 
            if temp_stack:
                stack.append(temp_stack)
            if temp_string:
                stack.append([temp_string])
            temp_stack=[]
            temp_string =''
        if char =='}':
            brace=0
            if temp_stack:
                stack.append(temp_stack)
            if temp_string:
                stack.append([temp_string])
            temp_stack=[]
            temp_string =''
        if char in alphabet and brace==1:
            temp_stack.append(char)
        if char in alphabet and brace==0:
            temp_string+=char
        if char!='}' and char==my_string[-1]:
            stack.append([temp_string])
    return stack
def main(my_string):
    my_list = generate_list(my_string)
    l = len(my_list)
    result_list = ['']
    for i in range(l):
        temp_list=[]
        for elt2 in my_list[i]:
            for elt1 in result_list:
                temp_list.append(elt1+elt2)
        result_list=temp_list
    return result_list
print(main("abcd"))
