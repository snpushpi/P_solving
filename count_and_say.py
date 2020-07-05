'''
	The count-and-say sequence is the sequence of integers with the first five terms as following:
	1.     1
	2.     11
	3.     21
	4.     1211
	5.     111221
	1 is read off as "one 1" or 11.
	11 is read off as "two 1s" or 21.
	21 is read off as "one 2, then one 1" or 1211.
	Given an integer n, generate the nth term of the count-and-say sequence. 
'''
def counter(string):
    temp_char = string[0]
    l = len(string)
    j = 1
    result_list = []
    if l==1:
        result_list.append((temp_char,str(j)))
    for i in range(1,l):
        if string[i]!=temp_char:
            result_list.append((temp_char,str(j)))
            j=1
            temp_char = string[i]
        else:
            j+=1
        if i==l-1:
            result_list.append((temp_char,str(j)))
    result_string = ''
    for i in range(len(result_list)):
        result_string+=result_list[i][1]+result_list[i][0]
    return result_string
def countandsay(n):
    temp_string = '1'
    for i in range(1,n):
        temp_string = counter(temp_string)
    return temp_string

print(countandsay(3))