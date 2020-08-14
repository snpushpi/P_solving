'''
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
Note:
A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:
Input:
rows = 2, cols = 8, sentence = ["hello", "world"]
Output: 
1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
Example 2:
Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
Output: 
2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
Example 3:
Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
Output: 
1
Explanation:
I-had
apple
pie-I
had--
The character '-' signifies an empty space on the screen.
'''
def main(sentence,rows,cols):
    count = 0
    row_count=0
    flag = False
    while row_count<=rows:
        temp = 0
        for char in sentence:
            if temp+len(char)<cols:
                temp+=len(char)+1
                if temp==cols:
                    row_count+=1
                    if row_count==rows:
                        flag = True
                        break
                    temp=0     
            elif temp+len(char)==cols:
                row_count+=1
                if row_count==rows:
                    flag = True
                    break
                temp=0
            else:
                row_count+=1
                if row_count==rows:
                    flag = True
                    break
                temp = len(char)
                if temp==cols:
                    row_count+=1
                    if row_count==rows:
                        flag = True
                        break
                    temp=0
                else:
                    temp+=1
        if flag:
            break
        count+=1
    return count
print(main(["hello", "world"],2,8))