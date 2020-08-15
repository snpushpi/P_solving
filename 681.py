'''
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
Example 1:
Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:
Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
'''
from itertools import product
def main(input_string):
    current_time = 60*int(input_string[:2])+int(input_string[3:])
    allowed = {int(x) for x in input_string if x!=':'}
    result = 24*60
    for i,j,k,l in product(allowed,repeat=4):
        hours, minutes = 10*i+j, 10*k+l
        if hours<24 and minutes<60:
            new_time = 60*hours+minutes
            diff = (new_time-current_time)%(24*60)
            if 0<diff<result:
                result = diff
                ans = new_time
    hour = ans//60
    mins = ans%60
    return str(hour)+':'+str(mins)
print(main("23:59"))