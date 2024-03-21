'''
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

 

Example 1:


Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        before_merge_count = 0
        after_merge_count = 0
        
        left_original = list1
        right_original = list1
        
        result = []
        result_right = []
        
        result.append(left_original.val)
        
        for i in range(b+1):
            if before_merge_count < a - 1:
                left_original = left_original.next
                right_original = right_original.next
                before_merge_count += 1
                result.append(left_original.val)
            else: 
                right_original = right_original.next
                
        left_original.next = list2
        
        while left_original.next:
            left_original = left_original.next
            result.append(left_original.val)
        
        left_original.next = right_original
        
        while left_original.next:
            left_original = left_original.next
            result.append(left_original.val)
        
        result_node = None
        
        for i in range(len(result)):
            new_node = ListNode(result.pop(), result_node)
            result_node = new_node
            
        return result_node
        