'''
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.
 
Example 1:
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:
Input: "AAABBC"
Output: 188
'''
import collections
def numTilePossibilities(Input):
    unique = set(Input)
    freq_dict = collections.Counter(Input)
    total_len=0
    while total_len< len(Input):
        temp_set=set()
        for char in Input:
            for comb in unique :
                temp_word = char+comb
                up_freq = collections.Counter(temp_word)
                flag = True
                for key, value in up_freq.items():
                    if value>freq_dict[key]:
                        flag = False 
                if flag:
                    temp_set.add(temp_word)
        unique|=temp_set
        total_len+=1           
    return list(unique)
print(numTilePossibilities("AAB"))

