'''
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)
Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.
 
Example 1:
Input: 20
Output: 4
Explanation: 
The confusing numbers are [6,9,16,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:
Input: 100
Output: 16
Explanation: 
The confusing numbers are [6,9,16,19,60,61,66,68,86,89,90,91,96,98,99].
 
Note:
1 <= N <= 10^9
'''
class Solution():
    def __init__(self):
        self.list = [1,6,8,9]
    def maker(self,N):
        maker_list=[0,1,6,8,9]
        Flag = True
        result_list = [1, 6, 8, 9]
        while True:
            temp_list=[]
            for elt2 in result_list:
                for elt1 in maker_list:
                    if elt2*10+elt1<=N :
                        temp_list.append(elt2*10+elt1)
                    else:
                        Flag = False
                        break
                if not Flag:
                    self.list+=temp_list
                    break
            if not Flag:
                break
            result_list=temp_list.copy()
            self.list+=temp_list
        
        #will remove the parts with just 1 and 8.
        final_list=[]
        for elt in self.list:
            if not set(str(elt)).issubset({'8','1','0'}):
                final_list.append(elt)
        print(final_list)
        print(self.list)
        return len(final_list)
c = Solution()
print(c.maker(20))
        
