'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = deque()
        
        if head:
            temp = head
            res.append(temp.val)

            while temp.next:
                temp = temp.next
                res.append(temp.val)

            sorted_node = None

            for i in range(len(res)):
                node = ListNode(res.popleft(), sorted_node)
                sorted_node = node

            return sorted_node
        else:
            return head