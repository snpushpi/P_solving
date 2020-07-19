'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.
 
Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
'''
def dulplicate(input):
    s = set(input[0])
    l = len(input)
    check_dict = {e:input[0].count(e) for e in s}
    for i in range(1,l):
        for elt in check_dict:
            check_dict[elt]=min(check_dict[elt], input[i].count(elt))
    result = []
    for elt in check_dict:
        for i in range(check_dict[elt]):
            result.append(elt)
    return result
print(dulplicate(["cool","lock","cook"]))