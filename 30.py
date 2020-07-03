'''
	You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
	Example 1:
	Input:
	  s = "barfoothefoobarman",
	  words = ["foo","bar"]
	Output: [0,9]
	Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
	The output order does not matter, returning [9,0] is fine too.
	Example 2:
	Input:
	  s = "wordgoodstudentgoodword",
	  words = ["word","student"]
	Output: []
'''
def findsubstring(s,words):
    count_dict = {}
    result_list = []
    for word in words:
        count_dict[word]= count_dict.get(word, 0)+1
    l = len(words[0])
    word_number = len(words)
    for j in range(n-l+1):
        seen_dict = {}
        i = 0
        while i<word_number:
            check_word = s[j+i*l:j+(i+1)*l+1]
            if check_word not in count_dict:
                break
            seen_dict[check_word] = seen_dict.get(word, 0)+1
            if seen_dict[check_word]>count_dict[check_word]:
                break
            i+=1
        if i==word_number:
            result_list.append(j)
    return result_list

