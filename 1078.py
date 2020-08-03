'''
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.
For each such occurrence, add "third" to the answer, and return the answer.
 
Example 1:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:
Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
 
Note:
1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.
'''
def text_checker(text,first, second):
    if not text:
        return []
    text_list = text.split(" ")
    l = len(text_list)
    result=[]
    i=0
    while i<=l-2:
        if text_list[i]==first and text_list[i+1]==second:
            if i+2<=l-1:
                result.append(text_list[i+2])
            i+=2
        else:
            i+=1
    return result
print(text_checker("alice is a good girl she is a good student", "a", "good"))
            

    