"""
STATEMENT
Given a string, find the length of the longest substring without repeating characters.
CLARIFICATIONS
- Contiguous substring, not subsequence, right? Yes. 
- Can the string be empty ? Yes.
EXAMPLES
"abcabcbb" -> 3 ("abc", starts at first)
"bbbbb" -> 1 ("b", single element substring)
"pwwkew" -> 3 ("wke", starts at middle)
COMMENTS
- We can keep a window of substring and grow/shrink it.
- The characters in the current string have to be remembered, set is good for that.
  Fast lookup, decent removal in size of the substring size.
- O(n) time complexity and O(n) space complexity.
- To do with constant space complexity, we may have to move to O(n^2) time complexity, by naively looking at every (i,j) position
  to check if that is a valid substring.
"""
def longest_substring(s):
    check_string = ''
    check_set = set()
    l = len(s)
    track_dict = {i:0 for i in range(l)}
    start = 0
    end = 0
    print(l)
    for i in range(l):
        if s[i] not in check_set:
            check_set.add(s[i]) 
            end +=1
            if i==(l-1):
                track_dict[start]=end
        else:
            substring = s[start:i]
            print(substring)
            track_dict[start]= end
            index = substring.rfind(s[i])
            start=index+1
            substring=s[start:i+1]
            check_set = set(substring)
            print(substring, check_set)
            end = len(check_set) 
    return track_dict
print(longest_substring('cabb'))


