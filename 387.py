'''
	Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
	Examples:
	s = "leetcode"
	return 0.
	s = "loveleetcode",
	return 2.
'''
def main(s):
    for index in range(len(s)):
        if s[index] not in s[:index]+s[index+1:]:
            return index
    return -1
print(main('loveleetcode'))
