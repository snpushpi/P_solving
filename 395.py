'''
    Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
    Example 1:
    Input:
    s = "aaabb", k = 3
    Output:
    3
    The longest substring is "aaa", as 'a' is repeated 3 times.
    Example 2:
    Input:
    s = "ababbc", k = 2
    Output:
    5
    The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''
def main(s,k):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char]+=1
        else:
            freq_dict[char]=1
    Flag = False
    for char in freq_dict:
        if freq_dict[char]<k:
            Flag = True
            break
    if not Flag:
        return len(s)
    Flag2 = False
    for char in freq_dict:
        if freq_dict[char]>=k:
            Flag2 = True
            break
    if not Flag2:
        return 0
    result = 0
    for index in range(len(s)):
        if freq_dict[s[index]]<k:
            result = max(result,max(main(s[:index],k), main(s[index+1:],k)))
    return result
print(main("aaabb",3))

