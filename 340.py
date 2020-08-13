'''
Given a string, find the longest substring that contains only two unique characters. For example, given "abcbbbbcccbdddadacb", the longest substring that contains 2 unique character is "bcbbbbcccb".
'''
def main(input_string):
    l = len(input_string)
    dp1 = {i:(0,{}) for i in range(l)}
    dp2 = {i:(0,{}) for i in range(l)}
    dp1[0]=(1,{input_string[0]})
    dp2[0]=(1,{input_string[0]})
    for i in range(1,l):
        if input_string[i] in dp1[i-1][1]:
            dp1[i]=(dp1[i-1][0]+1,{input_string[i]})
        else:
            dp1[i]=(1,{input_string[i]})
    for i in range(1,l):
        if input_string[i] in dp2[i-1][1]:
            dp2[i]=(dp2[i-1][0]+1,dp2[i-1][1])
        elif len(dp2[i-1][1])==1:
            new_set = dp2[i-1][1]|{input_string[i]}
            dp2[i]=(dp2[i-1][0]+1,new_set)
        else:
            dp2[i]=(dp1[i-1][0]+1,dp1[i-1][1]|{input_string[i]})
    maximum = 0
    index = 0
    for i in dp2:
        if maximum<dp2[i][0]:
            maximum = dp2[i][0]
            index = i
    return input_string[index-maximum+1:index+1]
        
print(main("abcbbbbcccbdddadacb"))


