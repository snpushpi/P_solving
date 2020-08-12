'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]
sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''
#We will build a segment tree
class Node():
    def __init__(self,val, start, end):
        self.sum = val
        self.left, self.right = None, None
        self.range = [start, end]
class SegmentTree():
    def __init__(self,size):
        self.root = self.build_segment_tree(0,size-1)
    def build_segment_tree(self, start, end):
        node = Node(0, start, end)
        if start>end:
            return None
        if start==end:
            return node
        mid = (start+end)//2
        node.left = self.build_segment_tree(start, mid)
        node.right = self.build_segment_tree(mid+1, end)
        return node
        
    def update(self,index,val, root=None):
        root = root or self.root
        if index<root.range[0] or index>root.range[1]:
            return 
        if index==root.range[0]==root.range[1]:
            return
        root.sum+=val
        self.update(index,val,root.left)
        self.update(index,val,root.right)

    def range_sum(self,start,end,root=None):
        root = root or self.root
        if end<root.range[0] or start>root.range[1]:
            return 
        if start<=root.range[0] and end>=root.range[1]:
            return root.sum
        return self.range_sum(start,end,root.left)+self.range_sum(start,end,root.right)

class NumArray():
    def __init__(self,nums):
        self.nums = nums
        self.segment_tree = SegmentTree(len(nums))
        for i in range(len(nums)):
            self.segment_tree.update(i,nums[i])
    def update(self,i,val):
        diff = val - self.nums[i]
        self.segment_tree.update(i,diff)
        self.nums[i]=val
    def sumrange(self,i,j):
        return self.segment_tree.range_sum(i,j)
