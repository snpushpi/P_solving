'''
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, /. Each operand may be an integer or another expression.
    Note:
    Division between two integers should truncate toward zero.
    The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
    Example 1:
    Input: ["2", "1", "+", "3", "*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
    Example 2:
    Input: ["4", "13", "5", "/", "+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6
'''
def arithmetic_list(num_list):
    track_list=[]
    for val in num_list:
        if val=='+':
            val1=track_list.pop()
            val2=track_list.pop()
            track_list.append(val1+val2)
        elif val=='-':
            val1 = track_list.pop()
            val2 = track_list.pop()
            track_list.append(val1-val2)
        elif val=='*':
            val1 = track_list.pop()
            val2 = track_list.pop()
            track_list.append(val1*val2)
        elif val=='/':
            val1 = track_list.pop()
            val2 = track_list.pop()
            track_list.append(int(val1/val2))
        else:
            track_list.append(val)
    return track_list[0]
        