'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
 
Example 1:
Input: low = 100, high = 300
Output: [123,234]
Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
'''
def generate(l):
    init = ''
    for i in range(1,l+1):
        init+=str(i)
    temp = init
    result = [init]
    while True:
        last = temp[-1]
        if last=='9':
            break
        last = int(last)+1
        temp=temp[1:]+str(last)
        result.append(temp)
    return result

def main(low,high):
    l1 = len(str(low))
    l2 = len(str(high))
    #now write a scheme for generating the sequence numbers of that length
    result = []
    for i in range(l1,l2+1):
        temp_list = generate(i)
        for elt in temp_list:
            if low<=int(elt)<=high:
                result.append(int(elt))
            elif int(elt)>high:
                break
    return result
print(main(1000,13000))