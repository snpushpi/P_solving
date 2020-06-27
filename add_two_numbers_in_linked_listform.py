"""
STATEMENT
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
CLARIFICATIONS
- Can there be leading zeros? No, except the number zero.
- I am confirming that the number of digits in the two numbers can be different? Yes.
EXAMPLES
(2 -> 4 -> 3), (5 -> 6 -> 4) -> 7 -> 0 -> 8
COMMENTS
- Since the numbers are given in reverse order, we only have to iterate the two linked lists and 
  accumulate the result in a new linked list.
- We should remember the carry.
- If one of the numbers end early, we should add the rest of the unfinished number added to the carry.
- O(m+n) time complexity and O(m+n) space complexity, where m and n are number of digits in the given numbers.
"""
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
def add_two_linked_list_numbers(l1,l2):
    return_val,carry = ListNode(0), 0
    num_l1, num_l2 = l1, l2
    while (num_l1.val is not None) and (num_l2.val is not None):
        to_add_val = num_l1.val+num_l2.val+carry
        if to_add_val>=10:
            carry =1
            to_add_val%=10
        else:
            carry = 0
        return_val.next = ListNode(to_add_val)
        return_val = return_val.next
        num_l1, num_l2 = num_l1.next, num_l2.next
    while num_l1.val is not None:
        to_add_val = num_l1.val + carry
        if to_add_val >= 10:
            carry = 1
            to_add_val %= 10
        else:
            carry = 0
        return_val.next = ListNode(to_add_val)
        return_val, num1_p = return_val.next, num_l1.next
    while num_l2.val is not None:
        to_add_val = num_l2.val + carry
        if to_add_val >= 10:
            carry = 1
            to_add_val %= 10
        else:
            carry = 0
        return_val.next = ListNode(to_add_val)
        return_val, num1_p = return_val.next, num_l2.next

        return return_val
    
    
    


