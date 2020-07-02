"""
STATEMENT
Given an array of words and a length L, format the text such that
each line has exactly L characters and is fully (left and right) justified.
CLARIFICATIONS
- Can we pack as much words as can in a sentence starting from the left? Yes, greedy approach is fine.
- Does the line last has to be taken care of separately? Words can be left-aligned in the last sentence 
  filled with spaces. Yes, that's an edge case (leetcode OJ does this too).
- Can a word length exceed the given length? No.
EXAMPLES
["This", "is", "an", "example", "of", "text", "justification."] ->
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""
def word_padder(word,space_num):
    i=0
    while i<=space_num:
        i+=1
        word+=' '
    return word
    

def padder(elt,L):
    l = len(elt[0])
    pad = L-l
    d = int(pad/(elt[1]))
    r = pad%(elt[1])
    words = elt[0].split()
    final_string = ''
    for j in range(len(words)-1):
        if j<r:
            final_string+=word_padder(words[j],d+1)
        else:
            final_string+=word_padder(words[j],d)
    final_string+=words[-1]
    return final_string        
        

def justifyText(list_of_strings,L):
    result_list = []
    temp_str = ''
    i=0
    for elt in list_of_strings:
        temp_str+=elt+' '
        print(temp_str)
        if len(temp_str)>L:
            if len(temp_str)==L+1:
                i+=1
                temp_str = temp_str[:-1]
                result_list.append((temp_str,'perfect'))
                temp_str=''
            else:
                temp_str = temp_str[:-(len(elt)+1)]
                result_list.append((temp_str, i))
                temp_str=elt+' '
                if elt == list_of_strings[-1]:
                    print('ji')
                    temp_str=temp_str[:-1]
                    result_list.append((word_padder(temp_str, L-len(temp_str)),'perfect'))
        else:
            i+=1
            if elt == list_of_strings[-1]:
                print('ji')
                temp_str=temp_str[:-1]
                result_list.append((temp_str, i-1))
    print(result_list)
    final_result_list = []
    for elt in result_list:
        if elt[1]=='perfect':
            final_result_list.append(elt[0])
        else:
            final_result_list.append(padder(elt,L))
    return final_result_list
print(justifyText(["This", "is", "an", "example", "of", "text", "justification", "and", "stay", "safe"],17))
        
