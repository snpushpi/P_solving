'''
	Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
	A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    phoneMap = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7' : 'pqrs', '8': 'tuv', '9':'wxyz'}
'''
def t_mapper(digis):
    phoneMap = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7' : 'pqrs', '8': 'tuv', '9':'wxyz'}
    final_result = ['']
    for char in digis:
        temp_result = []
        values = phoneMap[char]
        for prefix in final_result:
            for value in values:
                temp_result.append(prefix+value)
        final_result = temp_result
    return final_result

print(t_mapper('23'))

