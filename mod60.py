'''
In a list of songs, the i-th song has a duration of time[i] seconds. 
Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.
 
Example 1:
Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:
Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
Note:
1 <= time.length <= 60000
1 <= time[i] <= 500
'''
def mod(num_list):
    for i in range(len(num_list)):
        num_list[i]=num_list[i]%60
    print(num_list)
    result = 0
    for i in range(len(num_list)):
        if num_list[i]!=0:
            if 60-num_list[i] in set(num_list[i+1:]):
                count = num_list[i+1:].count(60-num_list[i])
                result+=count
        else:
            c = num_list[i+1:].count(0)
            result+=c
    return result
print(mod([30,20,150,100,40]))
