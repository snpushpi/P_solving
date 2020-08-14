'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
Note:
If n is the length of array, assume the following constraints are satisfied:
1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:
Input:
nums = [7,2,5,10,8]
m = 2
Output:
18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''
def main(nums,m):
    left, right= max(nums), sum(nums)
    while left<=right:
        mid = (left+right)//2
        count = 0
        temp= 0
        max_temp = 0
        for i in range(len(nums)):
            if temp+nums[i]<=mid:
                temp+=nums[i] 
                if i == len(nums)-1:
                    count+=1
                    max_temp = max(max_temp,temp)
            else:
                count+=1
                max_temp = max(max_temp,temp)
                temp=nums[i]
        if count==m:
            return max_temp
        elif count<m:
            right = mid
        else:
            left = mid
print(main([7,2,5,10,8],2))