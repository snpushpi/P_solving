'''
	Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
	Note: The input string may contain letters other than the parentheses ( and ).
	Example 1:
	Input: "()())()"
	Output: ["()()()", "(())()"]
	Example 2:
	Input: "(a)())()"
	Output: ["(a)()()", "(a())()"]
	Example 3:
	Input: ")("
	Output: [""]
'''
def validstring(string):
    count = 0
    for char in string:
        if char=='(':
            count+=1
        elif char==')':
            count-=1
        if count<0:
            return False
    return (count==0)

def main(input_string):
    l = len(input_string)
    queue = [input_string]
    visited = set()
    visited.add(input_string)
    level = False
    result = []
    while queue:
        new_str = queue.pop(0)
        if validstring(new_str):
            result.append(new_str)
            level= True
        if level:
            continue
        for i in range(len(new_str)):
            if not (new_str[i]==')' or new_str[i]=='('):
                continue
            part_string = new_str[:i]+new_str[i+1:]
            if part_string not in visited:
                visited.add(part_string)
                queue.append(part_string)
    return result
print(main("()())()"))

